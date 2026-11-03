# Mod-60 counter verification checklist

The Logisim counter is configured for a 6-bit output and maximum value 0x3B (decimal 59).

| Clock edge | Expected count |
|---:|---:|
| Initial/reset | 00 (decimal 0) |
| 1 | 01 |
| 2 | 02 |
| 9 | 09 |
| 10 | 10 |
| 58 | 58 |
| 59 | 59 |
| 60 | 00 (rollover) |
| 61 | 01 |

To demonstrate the minutes carry, connect the counter's terminal-count/carry output to the clock input of a second Mod-60 counter. The second counter should increment once when the first counter rolls over.
