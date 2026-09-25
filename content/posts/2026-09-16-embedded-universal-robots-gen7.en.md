---
title: "UR Gen 7: Quicker Arm, Smaller Brain"
seoTitle: "UR Gen 7 UR17g-1300 vs UR10e Cobot Specs Compared"
date: 2026-09-16T03:08:05+09:00
slug: "embedded-universal-robots-gen7"
summary: "Universal Robots unveiled its seventh-generation cobot platform, UR Gen 7, at IMTS 2026. We compare the UR17g-1300 to the previous-generation UR10e, which shares the same 1300 mm reach."
tags: ["Robot", "Global"]
categories: ["Deep Dive"]
cover:
  image: "/images/posts/embedded-universal-robots-gen7.en.png"
  alt: "Cover card: CB7 Core compute +40%, controller footprint -30%, UR17g-1300 top speed 5 m/s, unveiled at IMTS 2026 (Sept 14)"
  relative: false
draft: false
---

Universal Robots unveiled its seventh-generation collaborative robot platform, "UR Gen 7," on September 14 at IMTS 2026 in Chicago, one of North America's largest manufacturing trade shows. Three new arms arrive alongside a new controller and a redesigned tool flange, and the headline change is that cameras and force sensors can now plug straight into the wrist of the arm. Universal Robots describes it as an end-to-end redesign built on 20 years of cobot work and more than 100,000 industrial deployments, and frames the launch around "physical AI" — robots that pair vision and touch sensing with real-time control rather than just repeating a fixed motion path.

That framing matters for how to read this generation. Instead of one flagship arm, Universal Robots shipped three variants that trade payload for reach, all sharing the same controller and flange architecture. That lets an integrator pick the geometry a task needs — longer reach for a wide work cell, or more payload for a heavier tool — without switching software or rewiring the sensor stack.

## UR Gen 7

The three new g-Series arms carry their payload (kg) and reach (mm) right in the model name.

| Model | Payload | Reach | Weight | Repeatability | Max TCP speed |
|---|---|---|---|---|---|
| UR10g-1750 | 8 kg (10 kg extended) | 1750 mm | 44.7 kg | ±0.08 mm | 5 m/s |
| UR17g-1300 | 15 kg (17.5 kg extended) | 1300 mm | 40.7 kg | ±0.05 mm | 5 m/s |
| UR18g-950 | 18 kg | 950 mm | TBC | ±0.05 mm | 4 m/s |

Sources: [Universal Robots press release](https://www.universal-robots.com/news-and-media/news-center/universal-robots-unveils-gen-7-new-platform-industrial-automation-physical-ai/), [The Robot Report](https://www.therobotreport.com/universal-robots-launches-its-seventh-generation-robot-platform-at-imts/), [Unite.AI](https://www.unite.ai/universal-robots-debuts-gen-7-cobot-platform-for-physical-ai/)

The controller has been replaced by the "CB7 Core," which Universal Robots says delivers 40% more compute in a 30% smaller footprint than the previous generation. That extra compute has to go somewhere: the company positions it as headroom for running vision and force-sensing models locally, close to the arm, rather than shipping raw sensor data to an external PC.

Sources: [Universal Robots press release](https://www.universal-robots.com/news-and-media/news-center/universal-robots-unveils-gen-7-new-platform-industrial-automation-physical-ai/), [Automation World](https://www.automationworld.com/factory/robotics/news/55404812/universal-robots-unveils-gen-7-platform-at-imts-2026-in-chicago)

From an embedded-systems angle, the more interesting change is the new g-Series tool flange. It routes data, power, and safety signals to the end effector through a single connector at the wrist, so cameras and force sensors no longer need cabling run externally along the arm — a detail that matters a lot once you've had to route a MIPI or USB3 camera cable through a moving joint without it fraying. The arms themselves now ship with built-in force-torque sensing, impedance control, and Real-Time Data Exchange (RTDE), aimed at contact-sensitive tasks like precision assembly, where the arm needs to feel resistance and back off rather than push through it. The launch materials don't specify the exact voltage/current range the tool flange supplies or each model's peak power draw — those remain TBC, and worth confirming before designing a cabinet or power budget around one.

## UR17g-1300 vs. UR10e — same 1300 mm reach, different generation

We lined up the UR17g-1300 against UR10e, the previous generation's flagship at the same 1300 mm reach.

| Spec | UR10e (previous gen) | UR17g-1300 (Gen 7) |
|---|---|---|
| Payload | 12.5 kg | 15 kg (17.5 kg extended) |
| Reach | 1300 mm | 1300 mm |
| Weight | 33.5 kg | 40.7 kg |
| Repeatability | ±0.05 mm | ±0.05 mm |
| Max TCP speed | 4 m/s | 5 m/s |
| Max power draw | 615 W | TBC |

Sources: [Universal Robots UR10e tech sheet](https://www.universal-robots.com/manuals/EN/TechSheets/UR10e_techsheet_pdf_online/UR10e_techsheet_en.pdf), [Unite.AI](https://www.unite.ai/universal-robots-debuts-gen-7-cobot-platform-for-physical-ai/)

![Compared to the UR10e, the UR17g-1300 gains payload from 12.5 kg to 15 kg (17.5 kg extended) and top speed from 4 m/s to 5 m/s](/images/posts/embedded-universal-robots-gen7.en-compare.png "A bar chart of the table above. At the same 1300 mm reach, both payload and speed go up.")

At the same reach, payload rises 20% and top speed rises 25%, but the arm itself gets more than 7 kg heavier. That extra mass looks like the price of the new tool flange and built-in force-torque sensing; repeatability holds steady at ±0.05 mm.

## Who should care

Lines that bolt multiple cameras or force sensors onto the wrist — precision assembly, inspection, bin-picking with vision feedback — stand to gain the most from the simpler cabling the tool flange enables, and from having force-torque sensing built in rather than bolted on as a separate module. For a plain pick-and-place line with little sensing, the existing e-Series arms already do the job, and there's little reason to move to a heavier, likely pricier Gen 7 arm just for the extra controller headroom. Integrators already running RTDE-based force control on e-Series arms should find the migration path familiar, since the underlying control concepts carry over — it's the flange and controller hardware that changed, not the programming model. Pricing wasn't disclosed at launch.

## Availability in Korea

Universal Robots runs an official distributor network in Korea, but neither the launch materials nor any local distributor notice mentions a Korea launch date or price for UR Gen 7 yet — TBC.

## Verdict

UR Gen 7 changes the tool flange and controller more than it changes the arm itself. The emphasis on simpler wiring and easier sensor mounting points toward "physical AI" workloads that lean heavily on cameras and force sensing. The numbers that matter most for actually specifying a line — power draw and Korea pricing — are still missing, so anyone evaluating a purchase should wait for the full spec sheet.
