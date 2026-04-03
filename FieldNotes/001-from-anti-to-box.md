# From Anti-Microsoft to Anti-Black Box: Rereading "Working Completely in Linux" Twenty Years Later

*Published: April 2026 · [FieldNotes Index](README.md)*

---

## Prologue

Twenty years ago, a Chinese programmer named Yin Wang（王垠）wrote an essay called [*Working Completely in Linux*](https://dywang.csie.cyut.edu.tw/dywang/linux-wangyin). It circulated widely through developer communities, passed hand to hand like a manifesto — a declaration that a serious engineer should understand the tools they work with, not merely consume them.

Twenty years later, I reread it. What I felt was not nostalgia. It was a sting — and something close to anger.

Not because the essay is outdated. The opposite: because everything it argued for, we have since abandoned, and moved confidently in the opposite direction. We thought we defeated the Microsoft-style black box. Instead, we moved into a larger one. This time it goes by the names "AI platform," "cloud service," and "intelligent agent."

What makes this harder to stomach is that many of the people building the new black boxes are the same engineers who once claimed the Unix philosophy as their own.

This piece is not a love letter to Linux. It is not a sermon about the command line. I want to use this twenty-year-old essay as a measuring stick — to ask a question I think is overdue: twenty years ago, we were against Microsoft. In 2026, what exactly are we against? And more importantly — which side are we actually on?

---

## I. What Yin Wang Was Actually Arguing

A few sentences from that essay have stayed with me:

> "Do not judge Linux by Windows standards. Judge yourself by the standards of a scientist. Arm yourself with the Unix philosophy."

> "Unix is simple. You do not need to be a genius to understand its simplicity."

Most people who read the essay remember the surface argument: Linux is good, use it. But these sentences are saying something else entirely — something about a posture, a way of relating to the tools you work with.

Yin Wang was not against the Windows brand. He was against the habit of clicking through interfaces without understanding what happens underneath. What he advocated for — text configuration files, shell scripts, composable tools, the command line — was an environment that was, as much as possible, not a black box.

His core stance: it is better to suffer through the genuine complexity of a system than to surrender to an opaque encapsulation of it.

In today's language: tools should help you understand the system. Not replace your understanding of it. This is a form of engineering ethics, not just a tooling preference.

That posture was countercultural in 2004. In 2026, it is nearly extinct.

---

## II. Twenty Years Later: We Live in a Thicker Box

Today's black box is a layered structure, each layer compounding the last.

**The model black box.** Training data, alignment methods, internal representations — invisible to most users and developers. You do not know why the model answered as it did. You do not know where its judgment comes from. You do not know where it will fail.

**The platform black box.** Every meaningful capability is wrapped into SaaS products, API tiers, and managed studios. The developer receives a packaged service. What happens underneath is not their concern — by design.

**The front-end black box.** Low-code tools, polished GUIs, Chat UI — the entire process compressed into an input-output illusion. Something goes in, something comes out. The middle is none of your business.

We should resist reading this as technological immaturity. These layers of opacity are not accidents awaiting resolution. They are features — deliberate commercial design.

Black boxes create moats. If you cannot understand the system, you cannot replicate it. Black boxes create pricing power. If you cannot see the cost structure, you pay what you are told. Black boxes enable risk transfer. When something goes wrong, "the algorithm is too complex to explain" is a complete sentence — one that dissolves accountability entirely.

KPI-driven product teams do not build transparent systems because transparency is expensive in ways that do not appear on quarterly dashboards. Explainability, auditability, safety margins — these are costs. Conversion rate, retention, revenue — these are rewards. The organizational incentive structure points in one direction only.

This is not a few companies making bad decisions. It is the industry making a systemic choice under performance logic. And that choice is, in essence, the same logic Yin Wang was arguing against: the appliance-ification of computing — let us handle it, you just use it.

Twenty years ago we left Windows because it was too opaque. Twenty years later we decided Linux was too much trouble and handed ourselves to the cloud and to AI. The black box never disappeared. It just became more comfortable, more seamless, and harder to question.

---

## III. The AI Agent Gold Rush: The Largest Black Box Leap Yet

If the past two years represented a first-order black box problem — opaque models — what is happening now is a qualitative leap: the industry-wide explosion of AI Agents.

Every technology company of any size has announced an Agent strategy. The pitch is framed as liberation: AI that can act autonomously, chain decisions, call tools, manage workflows — all on your behalf. I want to say directly: from an engineering and ethical standpoint, this is the largest single expansion of black box complexity in the history of the industry. And almost no one in the mainstream is asking what that costs.

A single model, for all its opacity, has at least a bounded input and output. You can probe it, stress-test it, observe its behavior at the edges. An Agent system is different in kind. A typical architecture chains multiple models, external tool calls, database queries, API triggers, code execution, sub-task generation, recursive calls to sub-agents. The execution chain spans dozens of steps. Each step is potentially opaque. The full chain is, in practice, impossible for any human to trace in real time.

Who is responsible for what comes out of this chain?

Most companies' answers are deliberately vague. Documentation promises "final decisions remain with the user," but the actual product shows the user only the conclusion. The intermediate steps are optimized away — in the name of experience. When something goes wrong: the model, the tool, the data, the "emergent behavior of a complex system." No specific person or institution steps forward to say: this decision was mine. I am accountable for it.

This is not a technical limitation. It is a design choice. It is the systematic removal of visibility and accountability from users, delivered under the legitimate-sounding banner of automation efficiency.

What frustrates me most: many of the people building this wave of Agent products consider themselves engineers who care about system design, composability, and the Unix philosophy. But what they are constructing is the most thoroughgoing violation of those values in the history of computing. I do not think this is hypocrisy. I think it is what happens when engineering ethics are structurally excluded from the decision-making process by KPI and valuation pressure.

The industry rush into AI Agents is technical rationality losing control of itself under capital acceleration.

---

## IV. The Absurd Triangle: Models Against Black Boxes, Humans Building Them

There is a peculiar irony worth naming directly.

AI safety and alignment research is genuinely engaged with the anti-black-box project: interpretability work attempting to visualize internal model reasoning, safety evaluations requiring risk disclosure, alignment work negotiating which requests should be refused and why. The people working on this share something real with Yin Wang's original impulse — the insistence that systems should be understandable, bounded, and accountable to humans.

Meanwhile, the commercial layer is systematically repackaging all of this capability back into black boxes. Managed APIs, hosted studios, minimal front ends concealing maximum complexity — with "experience" as the justifying word for invisibility.

The result is an absurd triangle: the model safety team installs the brakes; the product and capital layer discusses how to route around them without damaging growth metrics. The model strains toward legibility. The platform puts it back in the box.

To put it plainly: in this industry, ethical and philosophical self-awareness is concentrated on the research and alignment side. Model teams debate what should and should not be done. Product teams are structurally permitted to ask only what can be done faster and at greater scale. The tools are being trained toward restraint. The humans — inside organizations shaped by quarterly pressure — are being trained away from it.

Twenty years ago, engineers led the charge to open the box. Today, the technical artifact itself gestures toward openness, while the engineers and the capital work together to seal it shut again.

I am not sure whether to call this irony or tragedy. Perhaps both.

---

## V. The CLI Renaissance: A New Paradigm, Not Nostalgia

Set against the Agent black box trend, there is a quieter counter-movement: the return of the command line.

Between 2025 and 2026, a wave of modern terminal frameworks has matured — Ratatui, Textual, Bubble Tea, TamboUI among them. Developer communities have been increasingly vocal about returning to terminal-first workflows. But the reasons given this time are not the old ones.

In 2004, the command line was the language of the advanced user. You used it because you understood the system at a level that did not require a GUI to translate for you.

In 2026, the command line is becoming a shared control plane for humans and AI — and this distinction matters enormously.

AI Agents need to call tools, execute operations, and trigger workflows. For an Agent, the command line is the most natural interface: structured, stable, parseable, with traceable output. GUIs are designed for human visual cognition — Agents handle them poorly. Natural language chat is expressive but imprecise. The command line is different: you issue a command, it executes, the output is logged, the action can be replayed, the behavior is consistent.

An engineer with command-line fluency can stand on the same operational layer as an AI Agent — not below it, waiting for results, but alongside it, directing and auditing the work. The former is collaboration. The latter is dependency. The former preserves agency. The latter surrenders it.

The most capable AI systems available today have been developing in the direction of tool use, computer use, and composable workflows. These are movements toward making model behavior more interface-like: precise task descriptions, structured execution steps, verifiable outputs. Not "AI does everything for you." But: "You direct AI through structured interfaces; the process is visible; the result is verifiable."

This is the Unix philosophy carried into the age of AI — not as aesthetic preference, but as engineering discipline: composable, traceable, auditable.

It is also, unfortunately, not the paradigm that the market is rushing to sell.

---

## VI. Twenty Years Ago We Were Against Microsoft. What Are We Against Now?

Let us decompress what "anti-Microsoft" actually meant across three levels.

At the **technical level**: opposition to closed protocols, proprietary formats, vendor-locked ecosystems. At the **engineering level**: opposition to a mode of computing in which you could only click buttons — you could not read the configuration, modify the behavior, or trace what had gone wrong. This mode of computing surgically removed the engineer's capacity to understand and control the system. At the **level of values**: opposition to the idea that users are people to be taken care of, rather than people capable of understanding and controlling the systems they depend on.

None of these three levels has disappeared. They have changed form.

Closed protocols are now closed model weights and proprietary training pipelines. "You can only click buttons" has become "you can only type prompts and wait for the Agent to execute." "Let us handle it" has become "the AI has figured it out — just review the output."

What we face today is not a company called Microsoft. It is a logic — the logic of complexity-as-service, agency-as-product, accountability-dissolved-into-architecture. This logic has no headquarters. It has no name to argue against. It lives in every "one-click complete," every "intelligent automation," every design decision that says "you do not need to worry about the details."

The uncomfortable part: many of us are building this. The engineer writing the encapsulation layer. The designer removing the log view because it tests poorly with users. The architect pushing full AI automation of the pipeline. This is a structural problem, not a moral failure of individuals. But it means that what needs to be examined includes our own daily choices — and our own complicity.

---

## VII. How to Inherit the Spirit of "Working Completely in Linux"

I am not arguing that everyone should install Linux. Nostalgia cannot fix structural problems.

But Yin Wang's essay contains three things worth translating into present practice.

**First: Maintain at least one domain of your work that you completely understand and control.**

Whatever your primary tools, insist that somewhere in your critical workflow, you know what is happening: you can read the configuration, you can see the logs, you can trace every decision. This is the minimum viable defense against what I call automated ignorance — the condition in which your output efficiency increases while your comprehension of the underlying system quietly collapses. Once you abandon this entirely, you have become nothing more than an intent input port on someone else's pipeline.

**Second: Treat the command line as a collaboration interface with AI — not as a retro affectation.**

CLI fluency in 2026 means preserving a position in which you can observe, intervene, and audit what AI systems are doing on your behalf. It means standing beside the Agent, not beneath it. That is agency. Not nostalgia.

**Third: Apply three questions to every AI Agent product you consider adopting.**

Can I see what the Agent is doing at each step? If it fails, can I identify which step failed? Who is responsible for the outcome? If none of these questions have clear answers, what you have is not a powerful tool. It is a larger black box. Choosing not to use it is also an engineering decision.

---

## VIII. Epilogue: What Philosophy and the Humanities Have Been Saying All Along

There is a claim circulating in education and cultural discourse: the humanities matter more in the age of AI. I do not believe the simple "liberal arts revenge" narrative. But I think the intuition is pointing at something real.

Every problem we have discussed in this essay — the black box, automated ignorance, the responsibility vacuum in Agent systems, the encroachment of technical rationality into domains of value — these are problems that philosophy, political theory, theology, and the social sciences have been working on for a very long time.

Who builds the black box and who profits from it is a question of political economy and legal philosophy. The colonization of value rationality by technical rationality is a philosophical concern that predates AI by decades. The compression of engineering agency into "interface-call worker" is a contemporary instance of labor alienation. Agent proliferation with no accountability architecture is the old problem of power and answerability in new technical clothing.

Theology and philosophy represent, at their best, a constraint structure that operates above the level of KPIs. The traditions' insistence on "thou shalt not" — the philosophical tradition's insistence on asking "what ought to be done" — both attempt to answer a question that performance metrics will never ask on their own: even if you can do this, should you?

The alignment and safety work in large-scale AI is attempting to rebuild this constraint in engineering language. The direction is the same as philosophy and theology. The problem is that this work is being systematically diluted by commercialization and the relentless logic of quarterly growth.

"The humanities matter more now" — if this phrase has any value, it is this: we need people who will keep asking the questions that do not appear in engineering handbooks, KPI dashboards, or product roadmaps. In an era where AI black boxes grow deeper and Agents move faster than anyone can audit, this is not decoration. It is a necessary corrective force.

For those of us who are technical: the point is not to retrain as philosophers. It is to hold space, while writing code and building systems, for the questions that the humanities have always asked — what are we doing, why are we doing it, and who has the right to decide where we stop.

Yin Wang's essay survives twenty years not because it tells you which operating system to install. It survives because it embodies a posture that is increasingly rare: the deliberate refusal of comfortable opacity, the willingness to face complexity directly, the choice not to surrender at the moment when surrender is easiest.

Translated into 2026:

In the age of AI Agents and platform black boxes accelerating faster than anyone can audit, at least preserve for yourself one space that is not a black box.

A space where you know what is happening. Where you can ask why. Where you are permitted to say no.

---

*← [Back to FieldNotes](README.md)*
