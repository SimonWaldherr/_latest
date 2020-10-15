--- 
extends: _layouts.post 
section: content 
image: https://techcrunch.com/wp-content/uploads/2020/10/koyeb-team01.jpg?w=600 
title: > 
  Koyeb raises $1.6 million for its serverless data-processing engine – TechCrunch 
description: > 
  French startup Koyeb has raised a $1.6 million (€1.4 million) pre-seed round.The company focuses on data-processing workflows across multiple cloud providers.In order to mix-and-match those various providers, Koyeb provides the serverless glue that ties everything together.Koyeb supports many different storage providers, such as AWS, Google Cloud, Microsoft Azure, Wasabi, Backblaze B2 as well as object storage products from DigitalOcean, Linode, Scaleway, Vultr, etc.You don’t have to manage your cloud infrastructure using Terraform and Kubernetes as Koyeb abstracts your infrastructure for you. 
date: 1602775207.4636798 
--- 
French startup Koyeb has raised a $1.6 million (€1.4 million) pre-seed round. The company focuses on data-processing workflows across multiple cloud providers. It hides many complexities using a serverless model.

Jean-David Chamboredon and Juliette Mopin from ISAI are leading the round with Plug and Play Ventures, Kima Ventures, AceCap and a long list of business angels also participating, such as Zachary Smith, Justin Ziegler, Alexis Lê-Quôc, Sébastien Lucas, Marc Jalabert, Amirhossein Malekzadeh, Philippe Besnard, Eric Ouisse, Dominique Vidal and Fabrice Bernhard.

Koyeb believes that companies will take advantage of the best cloud-native APIs and storage services going forward. In order to mix-and-match those various providers, Koyeb provides the serverless glue that ties everything together.

For instance, you can store videos on an object storage managed by DigitalOcean, transcribe the audio from those video files on Google Cloud using Google’s speech-to-text API and save the results on another object storage bucket.

You can move and process data based on a fixed schedule or based on events. For instance, when there’s a new file, you can trigger Koyeb with an API call. Everything scales automatically to process your task. And once your workflow is done, you no longer get billed for runtime.

Koyeb supports many different storage providers, such as AWS, Google Cloud, Microsoft Azure, Wasabi, Backblaze B2 as well as object storage products from DigitalOcean, Linode, Scaleway, Vultr, etc.

The company has also been working on a feature that lets you deploy your own Docker container so that you can build your custom functions. You can also push your function from GitHub directly.

This way, you don’t have to spin up new servers and shut them down later. You don’t have to manage your cloud infrastructure using Terraform and Kubernetes as Koyeb abstracts your infrastructure for you.