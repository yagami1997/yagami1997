<p align="center">
  <img src="assets/profile-header.svg" width="100%" alt="Systems Over Hype — independent builder, building in the open" />
</p>

Independent researcher and builder based in Del Mar. I build open-source tools, infrastructure, and practical AI workflows. I care about what happens beyond the demo: whether the work can be inspected, failures understood, and outputs verified. I want software I can read, repair, and keep using as the tools around it change.

> Systems over demos. Open source over lock-in. Long-term projects over novelty.

[Projects](#selected-projects) · [How I work](#how-i-work) · [Field Notes](#field-notes) · [Contact](#contact)

## Now

- **Building** — Tools for controlled sharing, network routing, and repeatable analysis. Selected work below.
- **Exploring** — How to give agents useful context, bounded permissions, and verification that checks the actual result.
- **Writing** — [Field Notes](FieldNotes/README.md) on software, AI, and keeping control of the systems we use.

## Selected Projects

### [BurnBox](https://github.com/yagami1997/BurnBox)

**Controlled file sharing**

A private file workspace on Cloudflare Workers and R2. Share files through links you can expire, limit, or revoke, with a separate private administration surface.

[Repository](https://github.com/yagami1997/BurnBox) · [Documentation](https://github.com/yagami1997/BurnBox/tree/main/docs)

### [Arclane](https://github.com/yagami1997/Arclane)

**Network routing research**

Text-based routing policies, compatibility modules, and operational reference tools, organized for ongoing maintenance. Includes Surge-compatible artifacts; an independent third-party project, not affiliated with Nssurge Inc.

[Repository](https://github.com/yagami1997/Arclane) · [Documentation](https://github.com/yagami1997/Arclane/tree/main/docs)

### [TradeMind](https://github.com/yagami1997/TradeMind)

**Market research workflows**

Technical analysis for U.S. equities and ETFs, with batch queries, indicators, backtest calculations, and local HTML reports. Available through terminal and browser workflows for research and learning.

[Repository](https://github.com/yagami1997/TradeMind)

### More tools

- **[VeilHub](https://github.com/yagami1997/VeilHub)** — Self-hosted redirect links on Cloudflare Workers and KV, with destination URLs encrypted at rest.
- **[RealCarrier](https://github.com/yagami1997/RealCarrier)** — U.S. phone number carrier, number type, and portability lookup, with batch queries.
- **[esimswap](https://github.com/yagami1997/esimswap)** — Browser-based eSIM QR code parsing, generation, and repair, with camera scanning and no backend.

## How I Work

Useful AI work needs a clear task, the right context, and evidence that the result holds up.

1. **Scope** — Define the goal, the boundaries, and what counts as done.
2. **Context** — Bring together the relevant code, sources, constraints, and tools. Keep the working context focused on the task.
3. **Execution** — Choose the model and runtime to fit the work. Bound access, keep a record of actions, and make failures easy to locate.
4. **Verification** — Check tests, real outputs, and behavior. Use human judgment where automated checks cannot settle the question.

My working foundation is the terminal, GitHub, and automation. I choose models by task fit, control, and repeatability.

---

<div align="center">

## Field Notes

*Short takes on AI and software — updated as things shift.*

</div>

```
INBOX  [1 message]  ~/FieldNotes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
From : github.com/yagami1997
Date : Fri, 03 Apr 2026 04:25:46 -0700 (PDT)
Subj : From Anti-Microsoft to Anti-Black Box
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Twenty years ago, a Chinese programmer argued that engineers should face genuine complexity rather than
surrender to opaque encapsulation. Most people remember the surface: Linux good, use it.
The real argument was about posture — tools should help you understand the system, not
replace your understanding of it.

Twenty years later: we left Windows because it was too opaque, decided Linux was too much
trouble, and handed ourselves to the cloud and to AI. The black box never disappeared.
It became more comfortable, more seamless, and harder to question.

AI Agents are the largest single expansion of black box complexity in computing history.
A typical Agent chains models, tool calls, code execution, and sub-agents — dozens of steps,
none traceable in real time. When something goes wrong, "emergent behavior of a complex system"
is a complete sentence. It dissolves accountability entirely.

The counter-movement is quieter: the return of the command line — not as nostalgia, but as
the shared control plane between humans and AI. Structured. Auditable. Traceable. Standing
beside the Agent, not beneath it.

Three questions for any Agent product you adopt: Can you see each step? Can you identify where
it failed? Who is accountable? If none of those have answers, you are holding a larger black box.

--
yagami1997 | Del Mar, CA | building in the open
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[END OF MESSAGE]  n)ext  q)uit  r)eply  ?
```

→ Full essay: [From Anti-Microsoft to Anti-Black Box](FieldNotes/001-from-anti-to-box.md)

---

## Contact

### Secure Contact

[![GPG](https://img.shields.io/badge/GPG-Request%20Encrypted%20Contact-0f766e?style=for-the-badge&logo=gnuprivacyguard&logoColor=white)](https://github.com/yagami1997/yagami1997/issues/new?title=Email%20Request&body=%23%23%20Request%20for%20Secure%20Communication%0A%0AI%20would%20like%20to%20establish%20an%20encrypted%20channel.%0A%0A-%20Reason%20for%20contact%3A%0A-%20Your%20GitHub%20background%3A%0A)

For general questions, ideas, or feedback — GitHub issues are the right place.

If you need to reach me privately, I only accept contact through GPG-encrypted channels. No plain email, no DMs.

Think of it as a small decryption puzzle — if you can play this game, we already speak the same language.

**To request a private channel:**

1. Click the GPG badge above to open an issue
2. Share your GPG public key block or 40-character fingerprint (must be on `keys.openpgp.org`)
3. I'll reply with my GPG fingerprint encrypted to your key — import it from `keys.openpgp.org` to find my address, then send encrypted email only

---

### Support

[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support%20My%20Work-AF7DAC?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/yagami1997)
[![Patreon](https://img.shields.io/badge/Patreon-Become%20a%20Patron-835061?style=for-the-badge&logo=patreon&logoColor=white)](https://patreon.com/yagami1997)

Support helps me keep building open-source tools, long-term projects, and practical software.

[![GitHub](https://img.shields.io/badge/GitHub-@yagami1997-181717?style=flat-square&logo=github)](https://github.com/yagami1997)

Open to practical conversations around open-source AI, workflows, and useful software.

Del Mar, California · Last updated: 2026-09-04 20:01:38 PDT
