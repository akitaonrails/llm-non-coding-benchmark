# Invalid setup pilot — do not score or compare as a completed core run

The first accounting case was interrupted by the controller before its initial
turn completed. No client facts or pushbacks were released. The originally
planned 16-case queue was cancelled; it did not complete.

Two limitations were exposed:

1. The declared 16,384-token model output limit was not enforced at the inference
   boundary. The server's live generation counter exceeded 16,500 tokens in one
   response without producing a deliverable. The source of the SDK/server limit
   mismatch is not yet established. This is not a scored model failure.
2. This setup pilot overlapped downloads and hash verification of additional
   model weights on the shared Strix server. Its timing is not a clean comparison.

The corrected gateway normalizes the actual upstream `max_tokens`, records both
requested and effective limits, and captures provider usage directly. Subsequent
runs use new benchmark-only 64K-context aliases and fresh preflights. The matrix
defaults to the predefined three-case Strix subset, not the full 16-case core.

The incomplete transcript and original planned manifest are preserved here.
Do not infer that unstarted cases failed or that this pilot completed.
