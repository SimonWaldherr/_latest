--- 
extends: _layouts.post 
section: content 
image: https://i.insider.com/5f7f714b4c3b2e0019bb9fd7?width=1200&format=jpeg 
title: > 
  How GM's $19 billion self-driving subsidiary Cruise trains its cars to have 'super-human' capabilities 
description: > 
  The $19 billion General Motors subsidiary Cruise relies on a continuous learning machine to help train all of its artificial intelligence-based algorithms.The data gleaned from each vehicle's 40 distinct sensors is fed into what Cruise calls its "continuous learning machine," also known as a CLM."Anytime we see something that goes wrong, that's a useful example," Harris said, of the data its cars collect.An example of the atypical events one of Cruise's self-driving cars can encounter in San Francisco.CruiseIn the early days of Cruise, the company didn't rely as heavily on machine learning as it does now, according to Harris. 
date: 1602368762.0190392 
--- 
Creating a fully-autonomous vehicle is one of the most difficult technological challenges facing developers today.

The machines have to be able to respond in milliseconds to litany of external sources, including other drivers on the road and pedestrian activity.

The $19 billion General Motors subsidiary Cruise relies on a continuous learning machine to help train all of its artificial intelligence-based algorithms.

And while much of the information gathered on-the-road by its 200-car fleet is typical driving behavior, the goal is to find the "needles-in-the-haystack" — like when a stoplight is out at an intersection.

"Anytime we see something that goes wrong, that's a useful example," Senior Manager Sean Harris told Business Insider. "Even if it's just wrong by a little bit, it's always a useful example."

Visit Business Insider's homepage for more stories.

On a typical day, a portion of the 200 self-driving cars in Cruise's fleet roam the streets of San Francisco, each for a few hours at a time, continually gathering data on road conditions, pedestrian activity, and the behavior of other drivers. While there are humans in the front-seat, the car is operating independently most of the time.

The data gleaned from each vehicle's 40 distinct sensors is fed into what Cruise calls its "continuous learning machine," also known as a CLM. This system is the key information source that can auto-label data collected by the cars to feed into all of of Cruise's artificial intelligence models.

At its core, Cruise — the $19 billion subsidiary of General Motors — relies on three different types of software to power its vehicles: perception, prediction, and planning. Perception is the "eyes" of the system: The technology that can pinpoint whether something is a car, a human, or another object. Prediction tries to decipher the future behavior of those objects, and planning incorporates both to help tell the vehicle how to perform.

And all of those programs are reinforced and made more powerful by the continuous learning machine, which is constantly updating the machines to reflect the latest data gathered by the vehicles.

Two Cruise workers — senior manager Sean Harris and principal research scientist Zhaoyin Jia — gave Business Insider a rare-glimpse into firm's strategy for perfecting its technology, details of which remain fairly hidden across the cadre of well-funded startups (and major corporations) that are hoping to commercialize their offerings.

Scaling to a '99 — 100%' solution

Programming a machine to follow the standard rules of the road would get about 80% of the way towards a fully-functional self-driving car, per Harris.

But 80% isn't nearly good enough to get a self-driving vehicle on the road, which is where the continuous learning machine comes in: "CLM has been really instrumental in us scaling up from an 80% solution to a true like 99-100% solution," Harris said.

Other drivers could violate standard protocols in a split second — think of a vehicle that has their left turn-signal on but makes a right turn — and the results could be catastrophic if the machine can't respond quickly. That's where the data from the cars comes in: It helps train the system for so-called "needles-in-the-haystack" events, or the atypical situations, like when the vehicle has to make a sudden stop because another car veered its the lane or the traffic lights go out at an intersection.

So when those adverse events happen — often requiring the human in the vehicle to take-over — the CLM helps quickly train the models on the new data, which is critical to getting the vehicles to fully-autonomous capabilities, where no humans are in the driver's seat.

"Anytime we see something that goes wrong, that's a useful example," Harris said, of the data its cars collect. "Even if it's just wrong by a little bit, it's always a useful example either to help us train our model better or validate something in the future."

And San Francisco is a great place to get that kind of data.

Cruise says its vehicles encounter challenging situations up to 46-times more often than other locations where autonomous car trials are underway — like Google's Waymo testing in the Phoenix suburbs.

An example of the atypical events one of Cruise's self-driving cars can encounter in San Francisco. Cruise

In fact, one minute of testing in the Bay area equates to an hour of testing in the suburbs, per the company. That's due to a number of factors, including a 16-times greater rate of encountering cyclists and significantly more construction sites, among others. Cruise's cars drove a total of 831,040 miles on California roads in 2019.

Read more: Waymo's head of lidar explains how the advanced laser tech went from science fiction to being a vital tool for self-driving cars

"We are trying to reach super-human performance on the road," added Jia, who joined Cruise earlier this year from Chinese competitor DiDi. "For these rare cases, you definitely need to accumulate a lot of mileage and training in order to have the model to be robust."

Zhaoyin Jia is a principal research scientist at Cruise. Cruise

In the early days of Cruise, the company didn't rely as heavily on machine learning as it does now, according to Harris. In fact, the CLM has only functioned as the core of the firm's operations for the past two years — but it has made a sizable impact on scaling the technology.

That's largely because it helps the company pinpoint the outlier instances when other vehicles don't behave as they should.

"The continuous learning machine is our approach to thinking about how we can take the less frequent, but still very important situations that we see on the road and scale our machine learning solutions out to those different problem areas," Harris said.