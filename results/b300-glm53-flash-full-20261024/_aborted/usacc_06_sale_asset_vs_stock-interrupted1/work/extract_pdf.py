import sys, re, zlib

def streams(data):
    """Yield (dict_body, decompressed_content) for every stream object."""
    for m in re.finditer(rb'<<(.*?)>>\s*stream\r?\n', data, re.S):
        hdr = m.group(1)
        sstart = m.end()
        send = data.find(b'endstream', sstart)
        raw = data[sstart:send]
        try:
            c = zlib.decompress(raw)
        except Exception:
            c = zlib.decompress(raw.rstrip(b'\r\n'))
        yield hdr, c

def load_objects(data):
    """Return dict objnum -> body bytes (dict+stream or raw dict)."""
    objs = {}
    for hdr, c in streams(data):
        if re.search(rb'/Type /ObjStm', hdr):
            N = int(re.search(rb'/N (\d+)', hdr).group(1))
            First = int(re.search(rb'/First (\d+)', hdr).group(1))
            pairs = c[:First].split()
            for k in range(N):
                num = int(pairs[2*k]); off = int(pairs[2*k+1])
                end = int(pairs[2*k+3]) if k+1 < N else len(c)
                objs[num] = c[First+off:First+end]
    # top-level objects (direct, with stream dicts)
    for m in re.finditer(rb'(?m)^(\d+) 0 obj\n(<<.*?>>)\n', data, re.S):
        num = int(m.group(1))
        if num not in objs:
            objs[num] = m.group(2)
            send = data.find(b'endstream', m.end())
            objs[num] = m.group(2) + b'\nstream\n' + data[m.end():send]
    return objs

def stream_of(objbody):
    starts = [m.end() for m in re.finditer(rb'stream\r?\n', objbody)]
    if not starts:
        return None
    endm = objbody.find(b'endstream')
    raw = data[endm:endm] if False else objbody[starts[-1]:endm]
    try:
        return zlib.decompress(raw)
    except Exception:
        return zlib.decompress(raw.rstrip(b'\r\n'))

def parse_cmap(content):
    cmap = {}
    for mm in re.finditer(rb'beginbfchar(.*?)endbfchar', content, re.S):
        for bm in re.finditer(rb'<([0-9A-Fa-f]{4})>\s*<([0-9A-Fa-f]+)>', mm.group(1)):
            src = int(bm.group(1), 16)
            try:
                cmap[src] = bytes.fromhex(bm.group(2).decode()).decode('utf-16-be')
            except Exception:
                cmap[src] = '?'
    return cmap

def extract(fname):
    data = open(fname, 'rb').read()
    objs = load_objects(data)
    pageobj = next(n for n, b in objs.items() if re.match(rb'\s*<<\s*/Type\s*/Page/', b))
    pagebody = objs[pageobj]
    contents = int(re.search(rb'/Contents (\d+) 0 R', pagebody).group(1))
    content = stream_of(objs[contents]).decode('latin-1')
    fnum = int(re.search(rb'/Font (\d+) 0 R', objs[int(re.search(rb'/Resources (\d+) 0 R', pagebody).group(1))]).group(1))
    fontmap = {}
    for fm in re.finditer(rb'/(\w+) (\d+) 0 R', objs[fnum]):
        name, fo = fm.group(1).decode(), int(fm.group(2))
        fb = objs[fo]
        toum = re.search(rb'/ToUnicode (\d+) 0 R', fb)
        cmap = parse_cmap(stream_of(objs[int(toum.group(1))])) if toum else {}
        fontmap[name] = cmap
    fontre = re.compile(r'/(\w+) [\d.]+ Tf')
    hexre = re.compile(r'<[0-9A-Fa-f]*>')
    tmre = re.compile(r'1 0 0 -1 ([\d.]+) ([\d.]+) Tm')
    i, n = 0, len(content)
    cur_font = None
    pending, res = [], []
    lasty = None
    while i < n:
        c = content[i]
        if c == '/':
            m = fontre.match(content, i)
            if m:
                cur_font = m.group(1); i = m.end(); continue
            i += 1; continue
        if c == '<':
            m = hexre.match(content, i)
            cmap = fontmap.get(cur_font, {})
            hexs = m.group(0)[1:-1]
            pending.append(''.join(cmap.get(int(hexs[k:k+4], 16), '')
                                   for k in range(0, len(hexs) - len(hexs) % 4, 4)))
            i = m.end(); continue
        if content.startswith('1 0 0 -1', i):
            m = tmre.match(content, i)
            if m:
                y = float(m.group(2))
                if pending: res.append(''.join(pending)); pending = []
                if lasty is not None and abs(y - lasty) > 1: res.append('\n')
                lasty = y
                i = m.end(); continue
        if c == ']':
            res.append(''.join(pending)); pending = []
            i += 1; continue
        i += 1
    if pending: res.append(''.join(pending))
    text = ''.join(res)
    lines = [re.sub(r'  +', ' ', l.strip()) for l in text.split('\n')]
    return '\n'.join(l for l in lines if l)

for f in sys.argv[1:]:
    print('=' * 20, f, '=' * 20)
    print(extract(f))
    print()
