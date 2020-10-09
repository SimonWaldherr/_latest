--- 
extends: _layouts.post 
section: content 
image: https://techcrunch.com/wp-content/uploads/2020/08/sofman-hou.jpg?w=711 
title: > 
  Waymo and TuSimple autonomous trucking leaders on the difficulty of building a highway-safe AI – TechCrunch 
description: > 
  TuSimple and Waymo are in the lead in the emerging sector of autonomous trucking; TuSimple founder Xiaodi Hou and Waymo trucking head Boris Sofman had an in-depth discussion of their industry and the tech they’re building at TC Mobility 2020.Hou and Sofman started out by talking about why they were pursuing the trucking market in the first place.“The market is massive; I think in the United States, $700-$800 billion a year is spent on the trucking industry.It’s continuing to grow every single year,” said Sofman, who joined Waymo from Anki last year to lead the effort in freight.But for local driving there’s actually no rules for interaction … in fact very different implicit social constructs to drive in different areas of the world. 
date: 1602212092.3707469 
--- 
TuSimple and Waymo are in the lead in the emerging sector of autonomous trucking; TuSimple founder Xiaodi Hou and Waymo trucking head Boris Sofman had an in-depth discussion of their industry and the tech they’re building at TC Mobility 2020. Interestingly, while they’re solving for the same problems, they have very different backgrounds and approaches.

Hou and Sofman started out by talking about why they were pursuing the trucking market in the first place. (Quotes have been lightly edited for clarity.)

“The market is massive; I think in the United States, $700-$800 billion a year is spent on the trucking industry. It’s continuing to grow every single year,” said Sofman, who joined Waymo from Anki last year to lead the effort in freight. “And there’s a huge shortage of drivers today, which is only going to increase over the next period of time. It’s just such a clear need. But it’s not going to be overnight — there’s still a really long tail of challenges that you can’t avoid. So the way we talk about it is the things that are hardest are just different.”

“It’s really the cost and reward analysis, thinking about building the operating system,” said Hou. “The cost is the number of features that you develop, and the reward is basically how many miles are you driving — you charge on a per mile basis. From that cost-reward analysis, trucking is simply the natural way to go for us. The total number of issues that you need to solve is probably 10 times less, but maybe, you know, five times harder.”

“It’s really hard to quantify those numbers, though,” he concluded, “but you get my point.”

The two also discussed the complexity of creating a perceptual framework good enough to drive with.

“Even if you have perfect knowledge of the world, you have to predict what other objects and agents are going to do in that environment, and then make a decision yourself and the combination knows is very challenging,” said Sofman.

“What’s really helped us is a realization from the car side of the of the company many, many years ago that in order to help us solve this problem in the easiest way possible, and facilitate the challenges downstream, we had to create our own sensors,” he continued. “And so we have our own lidar, our own radar, our own cameras, and they have incredibly unique properties that were custom designed through five generations of hardware that try to really lean into the kind of most challenging situations that you just can’t avoid on the road.”

Hou explained that while many autonomous systems are descended from the approaches used in the famous DARPA Grand Challenge 15 years ago, TuSimple’s is a little more anthropomorphic.

“I think I’m heavily influenced by my background, which has a tinge of neuroscience. So I’m always thinking about building a machine that can see and think, as humans do,” he said. “In the DARPA challenge, people’s idea would be: Okay, write a dynamic system equation and solve this equation. For me, I’m trying to answer the question of, how do we reconstruct the world? Which is more about understanding the objects, understanding their attributes, even though some of the attributes may not directly contribute to the entire self-driving system.”

“We’re combining all the different, seemingly useless features together, so that we can reconstruct the so-called ‘qualia’ of the perception of the world,” continued Hou. “By doing that we find we have all the ingredients that we need to do whatever missions that we have.”

The two found themselves in disagreement over the idea that due to the major differences between highway driving and street-level driving, there are essentially two distinct problems to be solved.

Hou was of the opinion that “the overlap is rather small. Human society has declared certain types of rules for driving on the highway … this is a much more regulated system. But for local driving there’s actually no rules for interaction … in fact very different implicit social constructs to drive in different areas of the world. These are things that are very hard to model.”

Sofman, on the other hand, felt that while the problems are different, solving one contributes substantially to solving the other: “If you break up the problem into the many, many building blocks of an AV system, there’s a pretty huge leverage where even if you don’t solve the problem 100% it takes away 85%-90% of the complexity. We use the exact same sensors, exact same compute infrastructures, simulation framework, the perception system carries over, very largely, even if we have to retrain some of the models. The core of all of our algorithms are, we’re working to keep them the same.”

You can see the rest of that last exchange in the video above. This panel and many more from TC Sessions: Mobility 2020 are available to watch here for Extra Crunch subscribers.