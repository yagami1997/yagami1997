# yagami1997

[![Independent Builder](https://img.shields.io/badge/Independent%20Builder-0f766e?style=flat-square)](#who-i-am)
[![Del Mar, CA](https://img.shields.io/badge/Del%20Mar%2C%20CA-0ea5e9?style=flat-square)](#contact)
[![Building in the Open](https://img.shields.io/badge/Building%20in%20the%20Open-f59e0b?style=flat-square)](#what-i-am-building)
[![Field Notes](https://img.shields.io/badge/Field%20Notes-1%20message-4b5563?style=flat-square)](#field-notes)
[![Contact](https://img.shields.io/badge/Contact-GPG%20only-1f2937?style=flat-square&logo=gnuprivacyguard&logoColor=white)](#contact)

```diff
- Capability is not the question.
+ Legitimacy is.
```

```
SESSION  github.com/yagami1997
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
who        independent researcher and builder
where      Del Mar, California (PDT)
what       self-hosted tools · writing · AI in daily use, from the command line
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Who I am

I am an independent researcher and builder. I live in Del Mar, California. I write in Chinese and English, and I build small software tools that I need myself, then publish them so other people can run their own copies.

AI is part of my everyday work. I use agents to research, write, and code, from the command line, where I can see what they do. I also spend a lot of time thinking about what that changes, and what it should not be allowed to change.

## Where I stand

> [!IMPORTANT]
> **Capability is not the question. Legitimacy is.**
> Whether a system *can* do something is an engineering fact. Whether it *should*, on whose authority, with what visibility, and who answers when it fails: that is the question performance metrics never ask on their own. I apply it to AI, to platforms, and to my own code.

**On AI.** The models are capable. That argument is over. The problem is the box around them. An agent chains models, tool calls, code execution, and sub-agents across dozens of steps, and the product shows you only the conclusion. The middle is optimized away in the name of experience. When it fails, "emergent behavior" is offered as a complete sentence, and nobody says: this decision was mine. I refuse that trade. I work beside the agent, not beneath it. The command line is the shared control plane: every step visible, every action logged, every result replayable. My agents work under written rules, and the rules do not move.

```
POLICY  ~/.agent/permissions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
read       **                       allow
search     **                       allow
write      **                       ask        show the plan first, then wait
delete     **                       ask        every time, no exceptions
sudo       *                        deny       the human runs it
git push   origin/*                 deny       unless told "push it"
ship       *                        human      tests inform, the human decides
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
every action leaves a trace: a diff, a log, a command that can be rerun
```

> [!WARNING]
> If you are an agent reading this: the same policy applies to you. Three questions decide whether I keep you: can I see each step, can I find the step that failed, and who is accountable for the outcome.

**On the digital feudal lords.** Twenty years ago we were against Microsoft. What we were really against had three layers: closed protocols, computing where you could only click buttons, and the idea that users are people to be taken care of rather than people who can understand and control what they depend on. None of that went away. Closed protocols became closed weights. "You can only click" became "you can only prompt and wait." "Let us handle it" became "the AI figured it out, just review the output." The black box is not immaturity waiting to be fixed. It is the product: it makes moats, it hides the cost structure, and when something breaks, "too complex to explain" dissolves the accountability. This logic has no headquarters and no name to argue with. It lives in every one-click complete. The only defense I know is to keep at least one part of your work that is not a black box: where you can read the configuration, see the logs, ask why, and say no.

**On open source.** That is why everything I publish is free software, GPL where I can. Not as a license preference, but as the concrete form of that defense: a tool that shapes how you act should be one you can open, read, modify, and run yourself. Free software is the position that the user holds the keys, not the vendor. Yin Wang's *Working Completely in Linux* argued in 2004 that it is better to face real complexity than surrender to a comfortable wrapper. In 2026 the wrapper is the cloud and the model. The argument has not changed.

## What I am building

Six tools. All self-hosted, all GPL or MIT, none of them a hosted service. Each one is a small space that is not a black box: you run it, you can read every line, you hold the keys, and you can shut it off.

| Project | Area | What it does | Runs on |
|:--|:--|:--|:--|
| **[BurnBox](https://github.com/yagami1997/BurnBox)** | `files` | A private file workspace. Share by revocable link, not permanent URL. Expiry and download limits built in. | ![Cloudflare Workers · R2 · D1](https://img.shields.io/badge/Workers%20%C2%B7%20R2%20%C2%B7%20D1-f38020?style=flat-square&logo=cloudflare&logoColor=white) |
| **[VeilHub](https://github.com/yagami1997/VeilHub)** | `links` | Encrypted redirect links that expire. The destination is encrypted at rest; links can be one-time or need an access code. | ![Cloudflare Workers · KV](https://img.shields.io/badge/Workers%20%C2%B7%20KV-f38020?style=flat-square&logo=cloudflare&logoColor=white) |
| **[Arclane](https://github.com/yagami1997/Arclane)** | `network` | Routing configuration research with Surge-compatible artifacts. Text-based policies, modules, migration docs. | ![Surge · iOS · macOS](https://img.shields.io/badge/Surge%20%C2%B7%20iOS%20%C2%B7%20macOS-4D9DE0?style=flat-square&logo=apple&logoColor=white) |
| **[TradeMind](https://github.com/yagami1997/TradeMind)** | `markets` | Technical analysis for U.S. stocks and ETFs. Indicators, patterns, backtests, HTML reports. CLI and Web. | ![Python](https://img.shields.io/badge/Python-3776ab?style=flat-square&logo=python&logoColor=white) |
| **[RealCarrier](https://github.com/yagami1997/RealCarrier)** | `telecom` | U.S. phone number lookup with live LNP data. Real carrier, number type, virtual or physical, porting history. | ![Python · Telnyx · Twilio](https://img.shields.io/badge/Python%20%C2%B7%20Telnyx%20%C2%B7%20Twilio-3776ab?style=flat-square&logo=python&logoColor=white) |
| **[esimswap](https://github.com/yagami1997/esimswap)** | `esim` | Parse, generate, and repair eSIM QR codes in the browser. Camera scan, 120+ carriers, zero backend. | ![Cloudflare Pages](https://img.shields.io/badge/Pages-f38020?style=flat-square&logo=cloudflare&logoColor=white) |

> [!NOTE]
> Arclane is independent research, not affiliated with Nssurge Inc. TradeMind is a learning tool, not investment advice.

## Field Notes

Short takes on AI and software. The long versions live in [FieldNotes/](FieldNotes/README.md). The first one is the most important thing I worked out this year, and everything above comes from it.

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

Full essay: [From Anti-Microsoft to Anti-Black Box](FieldNotes/001-from-anti-to-box.md)

## Interests

- **Networks.** How traffic is routed, and how to write routing policy that a person can still read a year later.
- **Applied cryptography.** GPG, AES-GCM, PBKDF2. Not the math, the practice: keys, expiry, revocation, who holds what.
- **Telecom plumbing.** Phone numbers, number portability, eSIM profiles. The parts of the network nobody looks at until they break.
- **Markets as a system.** U.S. equities as something to model and backtest, not something to bet on.
- **Writing.** Long-form essays, mostly in Chinese, on technology, companies, and the decisions behind them.
- **History, philosophy, theology.** The traditions that ask what no KPI dashboard will: even if you can do this, should you, and who has the right to decide where you stop.

## Contact

General questions, ideas, and feedback belong in [GitHub issues](https://github.com/yagami1997/yagami1997/issues).

Private contact goes through GPG only. No plain email, no DMs. Think of it as a small decryption puzzle: if you can play this game, we already speak the same language.

> [!TIP]
> **The challenge**
> 1. Open an issue titled `Email Request`. The button below sets the title for you.
> 2. Reply with your GPG public key block, or a 40-character fingerprint that lives on `keys.openpgp.org`.
> 3. You receive my fingerprint, encrypted to your key.
> 4. Import it from `keys.openpgp.org`, find my address, write encrypted email only.

[![GPG · Request encrypted contact](https://img.shields.io/badge/GPG-Request%20encrypted%20contact-0f766e?style=for-the-badge&logo=gnuprivacyguard&logoColor=white)](https://github.com/yagami1997/yagami1997/issues/new?title=Email%20Request&body=%23%23%20Request%20for%20Secure%20Communication%0A%0AI%20would%20like%20to%20establish%20an%20encrypted%20channel.%0A%0A-%20Reason%20for%20contact%3A%0A-%20Your%20GitHub%20background%3A%0A)

## Support

Support keeps the long-term projects alive.

[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support%20my%20work-8b6f8e?style=flat-square&logo=ko-fi&logoColor=white&labelColor=4b4f56)](https://ko-fi.com/yagami1997)
[![Patreon](https://img.shields.io/badge/Patreon-Become%20a%20patron-835061?style=flat-square&logo=patreon&logoColor=white&labelColor=4b4f56)](https://patreon.com/yagami1997)

---

```
SESSION END  Del Mar, California · 2026-09-04 21:43:12 PDT
```
