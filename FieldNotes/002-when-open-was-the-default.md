# When Open Was the Default

*Published: September 2026 · [FieldNotes Index](README.md)*

---

## The short version

Twenty years ago the network was open unless someone had a reason to close it. Today it is closed unless someone has a reason to open it.

That is the whole change. The rest of this note is examples.

I want to be careful about one thing up front. The early Internet was never a paradise. There were paywalls. There were firewalls. There were companies that kept their code secret. But those were the exceptions, and each one had to explain itself. Openness did not need an argument. Today it does.

---

## What "open" meant, in plain words

On September 27, 1983, Richard Stallman posted a message to a Usenet group. It began: "Free Unix!" Then: "Starting this Thanksgiving I am going to write a complete Unix-compatible software system called GNU (for Gnu's Not Unix), and give it away free to everyone who can use it."

The idea behind it was simple enough to say in one breath. If you have a program, you should be able to run it, read it, change it, and give a copy to your neighbor. He founded the Free Software Foundation in 1985 to defend that idea, and wrote the GNU General Public License in 1989 to put it into a contract.

By the early 2000s this idea had won more ground than anyone expected. In June 2001, Netcraft counted about 29 million web sites, and 63 percent of them ran Apache, a free web server anyone could download and read. Wikipedia went online on January 15, 2001. Creative Commons was founded the same year, so that writers and photographers could say "share this" in a way lawyers would respect. Any website could publish a feed, and any reader could follow it without an account, without asking.

None of this came from one company's generosity. It was a set of habits. You got the whole thing. You could read it. You could change it. You could pass it on. Software worked this way, and the network worked this way, because both were built by people who assumed it should.

---

## Five ordinary things, then and now

The clearest way to see a default flip is to look at ordinary tasks. Not at policy, at what you actually do.

### Installing a program

Then: you downloaded a file and ran it. Nobody approved. Nobody was asked.

On July 10, 2008, Apple opened the App Store with 500 apps. For the first time on a mainstream device, a company sat between you and every program you might want. The reasons were real. Phones carry your bank, your mail, your location. A review process stops a lot of harm.

But the decision moved. It used to be yours. Now it belongs to a queue you cannot see, following rules that change without notice, and the answer can be "no" for reasons you are never told. The rest of the industry followed. Today a device that lets you install anything you like is a niche product, and its owner is treated as a risk.

### Building on someone else's service

Then: a company with a service published a way for other programs to talk to it, and people built things. Twitter did this in 2006. Whole categories of software existed because of it.

In September 2012, Twitter released version 1.1 of its interface. Apps that "replicated the core Twitter experience" were capped at 100,000 users. In February 2023 the free tier ended entirely, with a week's notice, and the cheapest paid plan was set at 100 dollars a month. In June 2023 Reddit priced its own interface so that Apollo, the most popular independent Reddit app, would have owed about 20 million dollars a year. Apollo shut down on June 30.

I do not think either company was lying when it first opened the door. But look at the pattern. The door is open while the service needs builders to grow. It closes when the service is big enough that the builders are competition.

### Watching a video in a browser

Then: a browser was a program on your computer that showed you what a server sent. You could read every line of it.

On September 18, 2017, the World Wide Web Consortium, the body that writes the open standards of the web, published Encrypted Media Extensions as an official standard. Its purpose was to give copy protection a first-class place inside the browser. The same day, the Electronic Frontier Foundation resigned from the Consortium. Their letter said the Consortium was handing "a legally unauditable attack-surface to browsers used by billions of people."

The reason was plain. Studios would not put films on the open web without a lock. The Consortium decided the web needed the films more than it needed to stay fully open. So now there is a part of the program on your own computer that you are not allowed to look inside, and in some countries you can be prosecuted for trying. The body that once wrote "the web is for everyone" voted for that.

### Logging in to your bank

Then: a login asked for your name and password. Where you were sitting was not part of the question.

Today, many services look at your address before they look at your password. Banks and payment companies score the network you are connecting from. A shared address, a datacenter address, or an address in the wrong country can get your login refused, your account frozen, or a payment reversed. The reason is fraud, and fraud is real.

But notice what the network is now asking. Before it hears what you want, it asks where you appear to be. The address has become a credit score. And the refusal, when it comes, usually does not admit that it is a refusal. You see a blank page, a spinner, "something went wrong, try again later." The rule is there. It has just decided not to tell you it exists.

### Writing a program that reads the web

Then: in 1994, a webmaster named Martijn Koster proposed a small text file called robots.txt. A site could use it to say "please do not read these pages." It was a request, not a lock. Search engines honored it anyway, for about thirty years, because that was the custom.

In August 2023, The New York Times used that file to block OpenAI's crawler. Others followed. On July 1, 2025, Cloudflare, which sits in front of a large share of the web, announced it would block AI crawlers by default on every new site it serves. Site owners could opt back in, or charge for access.

I do not blame the publishers. AI companies took what they wanted without asking, and a polite request has no teeth against that. But look at where we landed. The last open commons of the web now starts locked. A new site begins with a gate. Thirty years of "please" ended in "no, unless."

---

## Stallman said this in 2010

On March 8, 2010, Stallman published an essay in the Boston Review. He was writing about what people were then calling "the cloud." He put it like this:

> "With SaaS, the users do not have even the executable file: it is on the server, where the users can't see or touch it."

And:

> "SaaS always subjects you to the power of the server operator."

When he wrote it, this sounded extreme. Gmail worked. Google Docs worked. Who cared where the program ran?

Fifteen years later, it describes nearly everything. Your mail, your documents, your photos, your code editor, and now the model that answers your questions all run somewhere you cannot see, under terms you did not write, that can change on a Tuesday. The first note in this series was about black boxes. This is the same box, seen from outside. You do not get a program you can read. You get permission to use one, for now.

The move from software to service was the move from "you have it" to "you may use it, on our terms, until we change them." That is a different relationship. It should have a different name. Stallman gave it one. Most people did not want to hear it.

---

## How I know the default flipped

I keep a public repository of network routing rules. They are plain text files that tell a computer which path a connection should take. I started it in June 2022. As I write this it has 439 commits.

Almost none of those commits add anything. Nearly every one is a repair. A service moved its servers. A login check got stricter. A name started resolving to a different kind of address, and a program that checks addresses stopped trusting it. Something that worked on Monday stopped on Thursday, and I went looking for which line had moved.

That repository is a log of other people's boundaries shifting. It exists because things break, and things break because somebody, somewhere, closed a door that used to be open. If the network still worked the way it did in 2001, the repository would have no reason to exist. I would prefer that.

I also have to say the other half. I write rules too. Every line in that repository says: this goes here, that goes there. Anyone who sets up a router, a firewall, or a name server is drawing lines for someone else. So the honest question is not "who gets to draw lines." Everyone does, including me. The question is what a line has to look like before I should accept it. Including my own.

---

## Three questions for any wall

Here is what I have settled on. When something on the network stops you, ask three things.

**Does it admit it exists?** A page that says "forbidden" is honest. A timeout that hides a rule is not. The worst boundaries are the ones dressed up as accidents, because you cannot argue with an accident.

**Does it tell you why?** "Your account is locked" is a fact. "Your account is locked because a login came from an address we do not recognize" is a reason. A reason can be wrong. A reason can be appealed. A fact just sits there.

**Can it end?** Does the rule have an expiry date, a review, a way to be lifted? A block that can never be undone is a verdict, and nobody signed it.

If a boundary passes all three, I can live with it, even when I dislike it. If it fails all three, what I am facing is not a rule. It is a wall that will not sign its name.

These questions apply to me. When a rule I wrote fails them, the rule is the problem, not the person it stopped.

---

## The same question, one level up

Stallman's 1983 question was small and concrete. Can you read this program? Can you change it? Can you give it to your neighbor?

It is time to ask the same three things about the network itself. Can you see the rule that stopped you? Can you do anything about where you stand? Can you pass on what you learned?

In 2001, the answer to all three was mostly yes, and nobody thought that was remarkable. Today the answer is mostly no, and nobody thinks that is remarkable either.

A default is a decision that has stopped announcing itself. Open was the default once, because people decided it should be. It stopped being the default because other people decided otherwise. Neither happened by accident. That means the next one will not happen by accident either.

---

*← [Back to FieldNotes](README.md)*
