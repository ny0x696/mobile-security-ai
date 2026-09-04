# Mobile Security AI

AI-agent skill system for authorized mobile application reverse engineering and bug-bounty research.

## What it does

- Routes APK/AAB/DEX, IPA/Mach-O, native libraries, APIs and traffic into specialized workflows.
- Uses evidence-first hypotheses instead of treating scanner output as proof.
- Correlates decompiled code, native boundaries and observed network traffic.
- Produces endpoint artifacts and reproducible validation scripts from observed evidence.
- Supports Android, iOS, native analysis, Frida/runtime work, API security and reporting.
- Enforces explicit authorization and scope before active validation.

## Flow

`Target -> Scope -> Case -> Static/Network/Native/Runtime -> Correlation -> Hypothesis -> Validation -> Evidence -> Finding -> Report`

## Layout

```text
SKILL.md
agents/          specialized agent contracts
workflows/       end-to-end workflows
schemas/         machine-readable case artifacts
tools/           tool adapters and operating notes
knowledge/       vulnerability and platform playbooks
templates/       evidence/finding/report templates
adapters/        OpenCode and Qoder integration
scripts/         local helper scripts
```

## Safety

Use only against apps, infrastructure and bug-bounty targets for which you have explicit authorization. Active validation must remain inside declared scope. Findings require evidence and provenance.

## License

MIT
