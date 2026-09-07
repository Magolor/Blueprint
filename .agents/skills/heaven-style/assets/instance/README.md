# Environment Instance Notes

Track reviewed non-secret environment references and observations when they help
future work. A machine name, home path, hardware capacity, or tool path is not a
credential. Do not ignore an entire note merely because it describes one machine.

- [Setup owner](setup.md) locates provisioning, profiles, maintenance, and recovery.
- [Machine observation](machine.md) records inspected facts for the named source
  machine. It is not evidence about the machine running a later session.
- [Docker owner](docker.md) routes service operations to the setup controller.

Keep each note scoped to a named machine or setup. Identify its source and limits.
Prefer links to a setup profile over a second writable settings inventory.
Verify relevant observations before acting on another machine or after setup changes.

Do not record passwords, API keys, access tokens, serial numbers, hardware UUIDs,
private key paths, or raw environment dumps. Keep credentials in the setup owner's
secret store. Keep transient probe output outside the distributed skill. Review
content before committing; a filename is not a security boundary.

`scripts/machine.py` writes to `~/.config/heaven-style/machine.md` by default.
Use `--output` to select a reviewed repository note deliberately. This keeps a
probe on a new machine from overwriting the distributed source-machine snapshot.
The installer preserves legacy `*.local.md` notes for compatibility, but those
notes are not current authority. Read these owner references first.
