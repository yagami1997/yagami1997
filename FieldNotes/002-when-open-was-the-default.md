# When Open Was the Default

*Published: September 2026 · [FieldNotes Index](README.md)*

---

## Something that worked yesterday

I keep a public repository of network routing rules. They are plain text files that tell a computer which path a connection should take. Much of the work is maintenance: a service moves, a login check changes, or two parts of the network stop agreeing about an address.

Something that worked on Monday stops on Thursday. I go looking for what changed.

Sometimes the answer is an ordinary mistake, including one of mine. Sometimes a security check is doing exactly what it should. Sometimes a service has changed who it will let in. From the user's side, these can look much the same: a page that will not load, a login that never finishes, a message asking you to try again later.

The repair begins with a question the screen has not answered: is this a failure, or a refusal?

That question has made me think differently about openness. A connection can be technically possible and still depend on permission from someone whose rules I cannot see. The [first note in this series](001-from-anti-to-box.md) was about understanding what happens inside a black box. This one is about what happens when the box will not let you in.

---

## What we expected to be able to do

When I say that open was once the default, I am thinking of a particular expectation: you could do useful things without first becoming someone's customer or asking a platform to approve them.

You could publish a website and link to another. You could follow a public feed in a reader you chose. With free software, you could read the source, change it, and pass on your changes. These freedoms were different, but they made room for the same kind of person: someone who could participate, build, and leave with more than an account.

This was never the whole Internet. Proprietary software, paid access, and restrictions were there too. Openness was something people worked to establish and defend. It was not a natural property of a network cable.

Richard Stallman's [announcement of GNU in 1983](https://www.gnu.org/gnu/initial-announcement.en.html) belongs to that work. He proposed a Unix-compatible system that people could freely share. The broader free-software commitment was concrete: users should be able to run a program, understand and change it, and give copies to others.

What matters to me is the relationship this creates. The developer gives you something you can keep working with. If the original author changes direction, you still have the code and the right to continue.

A service offers a different relationship. You can use it while the operator continues to provide access. It may be excellent, generous, and convenient. You still cannot maintain your own copy of the service merely because you have learned to depend on it.

In his [2010 essay on software as a service](https://www.bostonreview.net/articles/richard-stallman-free-software-drm/), Stallman made this loss of control central to his criticism. The operator runs the program and can change it. The user depends on decisions made elsewhere.

I do not need to agree with every conclusion he drew to recognize the problem. Convenience can make dependence easy to overlook. You discover how much control you gave up when the terms change.

---

## When access becomes dependence

A third-party app is a useful example. Its developer writes the interface, fixes the bugs, and earns the users' trust. But if the app relies on another company's service, that company can change the conditions under which the whole thing works.

In 2023, Apollo's developer [announced that the Reddit app would close](https://www.reddit.com/r/apolloapp/comments/144f6xm/apollo_will_close_down_on_june_30th_reddits/) after Reddit introduced new API pricing. An API is the interface that lets one program communicate with another. Apollo depended on it; its developer could not afford the proposed costs within the transition period. The app closed on June 30.

Charging for a service is not, by itself, a betrayal. Servers cost money. Access that is free today does not automatically carry a promise that it will be free forever.

But the dependence was unequal. A pricing decision by one company could end years of another developer's work. Users could keep the app on their phones, but they could not make the service behind it continue to answer.

That is the distinction I want to keep in view. Permission to build on a platform can be useful without giving a builder much lasting control. A growing ecosystem can look open while the power to determine its future remains with one operator.

Once people have built their work around that access, changing its terms is no longer just a private adjustment to a price list. Other people's time, work, and choices are involved. That deserves more consideration than the fact that the operator has the technical power to make the change.

---

## Some boundaries protect openness

There is a difficulty here that an argument against closed platforms has to face. People also need the right to refuse access to what they make.

In July 2025, Cloudflare [announced default blocking of AI crawlers for new sites using its service](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/). Website owners could choose to allow access. It was a visible change from assuming that automated access would be allowed to asking owners to authorize it.

It would be easy to count this as one more example of the web closing. But a publisher refusing an AI crawler is not the same as a platform preventing a user from choosing their own software. The publisher has work to protect. The crawler's operator has interests of its own. Calling both situations “closed” does not tell us whose freedom is at stake.

Being able to read an article does not settle every question about collecting it, reusing it, or building a business from it. The same is true of a photograph, a code repository, or a shared file. Openness needs terms under which people are willing to contribute. It cannot mean that the largest collector gets to decide what everyone else's work is for.

This is where I have to be more precise about my objection. I want people to retain a say in the systems they depend on and the work they share. Sometimes that requires access. Sometimes it requires a boundary. In either case, I want to know who makes the decision and what the affected person can do about it.

---

## The rules I write

My routing repository is a small place to apply that question.

It would be convenient to describe every repair as resistance to someone else's restriction. That would also be dishonest. Networks change for many reasons. A security check can reject an address because it is unsafe, because information is wrong, or because two systems interpret it differently. Making the request succeed is not enough to show that a repair was right.

I want to understand why it failed and restore the connection without removing a protection that still matters.

I also write rules. A routing configuration directs traffic along one path rather than another. A firewall permits some connections and refuses others. Those decisions have consequences for whoever uses the configuration, even when the file is public and the intention is helpful.

Publishing the rules makes them available to inspect. It does not automatically make them understandable or justified. I still have to explain what a rule does, why it is there, and when it should be changed or removed.

The same standard should apply to a service that blocks me. I do not expect every request to succeed. I expect a meaningful way to understand and question the decision.

---

## Three questions for a boundary

**Can I tell that a rule stopped me?**

A refusal should be distinguishable from a broken connection. If a deliberate block looks like a timeout, the user may spend hours repairing something that is working exactly as intended. The system does not have to reveal every detail of its defenses to acknowledge that access was denied.

**Can I understand the reason?**

“Your account is locked” describes the result. Saying that an unfamiliar login triggered a security check gives the user something to respond to. There may be details a service cannot safely disclose. It should still explain what it can and offer a useful next step. An explanation makes it possible to identify a mistake.

**Can the decision be reviewed?**

Some restrictions should expire. Others may need to remain. What matters is that a mistaken decision can be corrected, and that a rule can be reconsidered when its reason no longer applies. Review does not mean that every appeal must succeed. It means that being refused once does not remove your right to ask again with new evidence.

These questions do not make every boundary fair. They give us a place to begin examining it. They also apply to my own work. If a rule I wrote cannot meet them, I owe the person it affects a better explanation or a better rule.

---

## What I want to keep

I do not want to recreate an imagined Internet where nothing was restricted. I want to preserve the possibility of participating without giving up all control over how I participate.

Free software makes that possibility concrete: you can read, change, and share the program. Open protocols and portable data extend it: you can choose another tool or move your work. Clear rules and meaningful review matter where running your own copy is not an answer.

These are different freedoms. Together, they give people ways to act beyond accepting whatever an operator decides.

A default is a choice that has become familiar enough to go unquestioned. Open systems took work to build. They take work to keep open, including rules that protect the people contributing to them.

I want that work to leave the user with something they can do: understand a restriction, challenge a mistake, choose another tool, or continue on their own. A system can have good reasons to say no. It should not make the person hearing it powerless.

---

*← [Back to FieldNotes](README.md)*
