# impersonation
Simple Header-From Impersonation Detection supporting unicode transliterations.

# Write up

Impersonation is often one of the most-used tools by threat actors to gain access into your company. Often, their goal is to socially engineer the fooled employee to initiate wire transfers or provide their account credentials.

Seems like an easy problem to solve, right? The email security company should just see if they're faking a fellow employees name! Not quite. Most major email security vendors offer impersonation protection with various levels of effectiveness, let's explore some of the challenges behind impersonation protection.

One of the major issues is the craftiness of the threat actors. Knowing that impersonation protection was a growing market, many moved away from simple impersonation, and started employing simple obfuscation techniques to throw off automated systems. You may ask yourself, who is going to fall for an email from "Jẚmës Sḿi7h", and believe it's from their boss James Smith? The unfortunate truth is thousands will. Whether its due to their email client automatically converting unicode characteres to ascii, or they just quickly glanced at their phone, these messages will end up fooling someone.

In a three-hour code write, I demonstrate a simplistic impersonation protection solution that can detect David Miŀḷ3ṝ as being David Miller, ĵessicẩ Wҕιt3 as Jessica White, and more:

https://github.com/cxmplex/impersonation

As I limited myself on time, I employed a standard replacement method. For each unicode character set/block, I created a mapping of their ascii (A-Za-Z) letter to their unicode special character. This included cyrillic, greek, coptic, latin diacritics, and 1337speak. 

To envision this map in a non-technical way, here's an example: The letter A also looks like the number 4, and it can also look like any of these ḀẠẢẤẦẨẪẬẮẰẲẴẶ. What I did is create a list, saying here's all the different letters and symbols that look like the letter A.

This allows us to transform Miŀḷ3ṝ to Miller, and ĵessicẩ to Jessica.

Now here's where it gets even harder. Who's to say Jessica White doesn't go by Jess White, and David Miller doesn't go by Dave Miller. The "sciency" term for a pet name is a hypocorism. Here's an example:

John can be Johnny, or Johnnie, or Jony. The inverse is also true (where johnny can be john), requiring us to programatically reverse our hypocorism list as well to test for the reverse.

So we've determined how to take ĵessicẩ and turn it into jessica, and we've determined that jessica can also be jess or jessie, but what if they've simply mispelled the name? This is another common trick they'll do.

Rather than ĵessicẩ we have ĵesicẩ or ĵessicẩ or ĵessiccẩ. To counter this trick, I employed a metric called levenshtein distance. Levenshtein distance essentially measures the difference between two words. If I give it the word "ball" and the word "mall", the distance is 1, because B has been replaced with M (a substitution), you also measure additions and deletions as well, (deletion: bal vs ball is 1, addition and substitution: bald vs balll is 2, substitution: bald vs beat is 3).

By setting a threshhold based on the length of the name, I'm able to confidentally say that jesssica is "close enough" to jessica, and perform the match.

Results

The names could be represented in the from header as the following, and still be matched:

Jẚmës Sḿi7h
Sḿi7h, Jẚmës
ĵessicẩ Wҕιt3
David Miŀḷ3ṝ
Emiŀу ||| ḿ0or3

After Deobfuscation & Normalization:
james smith
smith james
jessica white
david miller
emily moore

Given the employee John Smith, the following deobfuscated names would be matched, showing that the order of the name isn't necessarily important:

johnny smith
johnnysmith
smith johnny
smith john
smithjohn
smithjohnny
johnnysmithy
johnsmithy
smith johnnyson

While these would exceed the allowed tolerance, despite sometimes containing the name itself (for instance johnannson contains john, and smithers contains smith):

smithers johnannson
johannson smithers
johnannson smithers

Even though the capabilities in this 3-hour project are quite cool, there are still many ways a threat actor might try to get around this. This is why email-security companies have put so much focus into their impersonation protection products detection capabilities, offering continous improvements, as threat actors get more clever by the day.

# Building

This is a dockerized application. Building and running it is as simple as:

`docker build -t impersonation .`

`docker run -p 8080:8080 impersonation`

# Testing

This project comes with several pre-written functional unit tests (it was TDD for the most part), but I did not create a "test runner". You can manually invoke any of the tests (make sure CWD is project root for imports to resolve).
