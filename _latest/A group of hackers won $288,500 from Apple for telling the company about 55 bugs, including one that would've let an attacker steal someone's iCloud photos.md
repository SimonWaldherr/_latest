--- 
extends: _layouts.post 
section: content 
image: https://i.insider.com/5f806630ea74820019ca6257?width=1200&format=jpeg 
title: > 
  A group of hackers won $288,500 from Apple for telling the company about 55 bugs, including one that would've let an attacker steal someone's iCloud photos 
description: > 
  Five "white hat" — or ethical, non-malicious — hackers spent three months hacking Apple and uncovered 55 vulnerabilities in the process.Apple fixed the vulnerabilities almost immediately after they were disclosed, the hackers said.They were operating as "white hat" hackers, meaning their goal was to alert Apple to the vulnerabilities rather than to steal information.Curry said that once Apple processes and rewards all of the bugs the group reported, their total payment may exceed $500,000.Read the full report on the white hat hacker team's findings here. 
date: 1602265104.652825 
--- 
Five "white hat" — or ethical, non-malicious — hackers spent three months hacking Apple and uncovered 55 vulnerabilities in the process.

They won $288,500 in bounties from Apple in exchange for disclosing the bugs.

Eleven of those vulnerabilities were labeled "critical," including one that would have let hackers steal all the files and photos stored in a victim's iCloud account before infecting that person's contacts.

Apple fixed the vulnerabilities almost immediately after they were disclosed, the hackers said.

Visit Business Insider's homepage for more stories.

A group of hackers spent months targeting Apple's sprawling online infrastructure and found a slew of vulnerabilities — including one that would allow hackers to steal files from people's iCloud accounts — they announced in a blog post this week.

They were operating as "white hat" hackers, meaning their goal was to alert Apple to the vulnerabilities rather than to steal information. The team was led by 20-year-old Sam Curry, along with Brett Buerhaus, Ben Sadeghipour, Samuel Erb, and Tanner Barnes.

"I had never worked on the Apple bug bounty program so I didn't really have any idea what to expect but decided why not try my luck and see what I could find," Curry said in the blog post. "Even though there was no guarantee regarding payouts nor an understanding of how the program worked, everyone said yes, and we began hacking on Apple."

Apple has paid the group $288,500 so far through its bug bounty program in exchange for disclosing 55 vulnerabilities, 11 of which were labeled as "severe." Curry said that once Apple processes and rewards all of the bugs the group reported, their total payment may exceed $500,000.

One of the most egregious vulnerabilities that the group found would have allowed hackers to build a worm that steals people's iCloud files before infecting the iCloud accounts of their contacts. The vulnerability hinges on the fact that Apple Mail is supported by iCloud — the white hat hackers were able to compromise iCloud accounts after sending an email to an iCloud.com email address that contained malicious code.

Apple patched all of the vulnerabilities shortly after they were reported, Curry said.

In the process of seeking out the bugs, Curry and his team gained insight in the massive scale of Apple's online infrastructure. Apple owns more than 25,000 web servers, which fall under Apple.com, iCloud.com, and over 7,000 other unique domains, the researchers found. Many of the vulnerabilities were discovered by searching through obscure web servers owned by Apple, like its Distinguished Educators site.

Cybersecurity experts who reviewed the research by Curry's team said that, while some of the severe vulnerabilities are concerning, they reflect inherent challenges that should be expected for a company maintaining such huge online infrastructure.

"The breadth of issues identified within the vast Apple online presence ... actually is more evidence of how difficult it is to keep on top of all security issues as organisations grow than a negative reflection of any security practices within Apple," Tim Mackey, principal security strategist at the Synopsys Cybersecurity Research Center, told Business Insider.

Apple did not immediately respond to a request for comment.

Read the full report on the white hat hacker team's findings here.