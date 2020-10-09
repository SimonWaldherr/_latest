--- 
extends: _layouts.post 
section: content 
image: https://techcrunch.com/wp-content/uploads/2020/10/GettyImages-1191500603.jpg?w=600 
title: > 
  How Roblox completely transformed its tech stack – TechCrunch 
description: > 
  Picture yourself in the role of CIO at Roblox in 2017.At a time when users have precious little patience for outages, your uptime was just two nines, or less than 99% (five nines is considered optimal).Unbelievably, Roblox was popular in spite of this, but the company’s leadership knew it couldn’t continue with performance like that, especially as it was rapidly gaining in popularity.The company needed to call in the technology cavalry, which is essentially what it did when it hired Dan Williams in 2017.When Roblox approached him in mid-2017, he jumped at the chance to take on another major infrastructure challenge. 
date: 1602274061.3063197 
--- 
Picture yourself in the role of CIO at Roblox in 2017.

At that point, the gaming platform and publishing system that launched in 2005 was growing fast, but its underlying technology was aging, consisting of a single data center in Chicago and a bunch of third-party partners, including AWS, all running bare metal (nonvirtualized) servers. At a time when users have precious little patience for outages, your uptime was just two nines, or less than 99% (five nines is considered optimal).

Unbelievably, Roblox was popular in spite of this, but the company’s leadership knew it couldn’t continue with performance like that, especially as it was rapidly gaining in popularity. The company needed to call in the technology cavalry, which is essentially what it did when it hired Dan Williams in 2017.

Williams has a history of solving these kinds of intractable infrastructure issues, with a background that includes a gig at Facebook between 2007 and 2011, where he worked on the technology to help the young social network scale to millions of users. Later, he worked at Dropbox, where he helped build a new internal network, leading the company’s move away from AWS, a major undertaking involving moving more than 500 petabytes of data.

When Roblox approached him in mid-2017, he jumped at the chance to take on another major infrastructure challenge. While they are still in the midst of the transition to a new modern tech stack today, we sat down with Williams to learn how he put the company on the road to a cloud-native, microservices-focused system with its own network of worldwide edge data centers.

Scoping the problem