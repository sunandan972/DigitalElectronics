# State Table

| Present state | Condition | Next state |
|---|---|---|
| CLOSED (00) | V·P = 0 | CLOSED (00) |
| CLOSED (00) | V·P = 1 | OPENING (01) |
| OPENING (01) | T = 0 | OPENING (01) |
| OPENING (01) | T = 1 | OPEN (10) |
| OPEN (10) | T = 0, either O | OPEN (10) |
| OPEN (10) | T = 1, O = 1 | OPEN (10) |
| OPEN (10) | T = 1, O = 0 | CLOSING (11) |
| CLOSING (11) | O = 1, either T | OPENING (01) |
| CLOSING (11) | O = 0, T = 0 | CLOSING (11) |
| CLOSING (11) | O = 0, T = 1 | CLOSED (00) |

RESET=1 forces the state to CLOSED (00).
