# Lance Dube — Learning Log
**Programme:** Fusion Group Technologies Junior Developer Training (FTC 001)

---

## Week 1

### Day 1 — Environment Setup
- Installed: VS Code, Python 3.12, Node.js, Git, SQL Server Express, SSMS
- Completed Checkpoint 0

### Phase 1 — Python Fundamentals

**Completed:**
- Block A: Variables, data types, if/else, loops, functions
- Block B: Number guessing game ✅
- Block C: Movie watchlist (list of dictionaries practice)
- Block D: Ticket list filtering, counting, sorting with lambda
- Block E: JSON file saving/loading, contact book ✅

**Key things that tripped me up:**
- while True loop must be inside main(), not outside it
- Loop variable (movie) is one item, not the whole list (movies)
- .lower() needs brackets — .lower without () does nothing
- delete_contact must use the right variable name (to_delete, not name)
- if __name__ == "__main__": goes at module level, no indentation

**Git repo:** https://github.com/lance-sd/fusiondesk-training

---

## Phase 1 wrap-up: log analyser, classes, self-review

**What I did**
- Finished `log_analyser.py` (read_log, analyse_log, write_report, main). Output checked: 5 errors + 3 warnings + 7 info = 15 total lines.
- Built a `Ticket` class with `__init__`, `close_ticket()` and `__str__`.
- Did one self-review task per block (A to E): age calculator, FizzBuzz, `safe_divide`, highest score from a list of dicts, `BankAccount`.

**What broke and how I fixed it**
- `return` inside a `for` loop exited after the first line. Fix: dedent the `return` so it runs after the loop.
- `in lines` instead of `in line`. I was checking the whole list, not the current item.
- `range(1, 50)` stops at 49. Fix: `range(1, 51)` to include 50.
- Calculated a value but never stored or returned it (`safe_divide`, `BankAccount`). Fix: assign to `self.balance` or `return` the result.
- `def init` instead of `def __init__` (missing double underscores).

**Concepts that clicked**
- Parameters bring data IN. Unpacking a return value (`a, b, c = func()`) catches data coming OUT. They are separate mechanisms.
- Lists and dicts are mutable, so a function can change them without returning. Numbers and strings are immutable, so a function has to `return` the new value.
- A class bundles data (attributes) and behaviour (methods) together.

---

## Phase 2: SQL Server

**What I did**
- Designed FusionDesk: Clients, Users, Tickets. Both foreign keys sit in Tickets.
- Created all three tables, loaded 5 clients, 3 users and 15 tickets, and wrote the four required queries plus a JOIN query.

**What broke and how I fixed it**
- Created the first table in `master` by mistake. Fix: `CREATE DATABASE FusionDesk`, `USE FusionDesk`, drop the stray table.
- Ran an INSERT twice and got duplicates. Fix: preview with `SELECT ... WHERE ClientID >= 6`, then `DELETE` with the same `WHERE`.
- `Status varchar(10)` was too short for "In Progress" and "Waiting for parts". Fix: `ALTER TABLE ... ALTER COLUMN Status varchar(20)`.
- Subtracting two `DATE` columns gave error 8117. Fix: `DATEDIFF(day, CreatedDate, ClosedDate)`.
- `AVG` of whole numbers returned 1 instead of 1.1667 (integer truncation). Fix: multiply by `1.0` inside the `AVG`.
- Foreign key test: inserting `ClientID = 99` was rejected with error 547. The foreign key is enforced, not just documentation.

**Concepts that clicked**
- Normalisation: store each fact once. Otherwise one change means updating many rows (update anomaly).
- Use a meaningless auto-increment ID as the primary key, not email, because a changing key breaks every foreign key that points to it.
- `IDENTITY` never reuses numbers, so gaps from failed or deleted inserts are normal.
- Apostrophes inside text are doubled: `can''t`. Dates are `YYYY-MM-DD`.
- `JOIN` (inner) only returns rows with a match on both sides. `LEFT JOIN` keeps every row from the left table. Use `LEFT JOIN` when the question is "show me every client". `COUNT(TicketID)` gives 0 for a client with no tickets, but `COUNT(*)` would wrongly give 1.
- SSMS red squiggles can be stale IntelliSense. The truth is the status bar and the Messages tab, not the Error List.
- "Query executed successfully" only means the syntax was valid. Check the actual result.

---

## Git

**What I did**
- 14 commits on `lance-sd/fusiondesk-training`: Python work, the three CREATE scripts, the three INSERT scripts, `Queries.sql` and `TicketsPerClient.sql`.

**What broke and how I fixed it**
- A commit message said "SQL scripts" but the commit only held `Progress.py` and `test.py`. `git status` before `git add` would have shown this.
- Ran `git status` in a folder outside the repo (`fatal: not a git repository`). Fix: move the files inside `C:\Code\Phase 1\`.
- `git add` failed on a filename that did not exist, and I ran commit and push anyway. Both did nothing. If a command ends in `fatal:`, stop.
- Three empty commits in a row: I added `Queries.sql` while the changed file was named `SQLQuery2.sql`, then `TicketsPerClient.sql`. The name in `git add` must match what `git status` lists.

**Habit to keep**
- Always: `git status`, read it, `git add <the file status listed>`, `git status` again (green?), `git commit`, `git push`.

---

## Still to do
- Book Checkpoint 1 (contact book + log analyser) with Warren.
- Practise the Checkpoint 2 whiteboard: draw the three tables and both relationships from memory, then run all five queries live.
