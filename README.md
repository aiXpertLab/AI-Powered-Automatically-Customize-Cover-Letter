### AI-Powered Automatically Customize Cover Letter for Each Job Post
> - AI-Powered, Customized, Cover Letters
> - AI Assistant Job Flow Automator. 
> - Automate the customization of cover letters tailored to your resume and the unique requirements outlined in the job description extracted.

<div align="center">

<a href='https://www.hypech.com'>
<img src="src/aiCL/resources/images/ai_powered_long.png" alt="AI-Powered Cover Letter" height=300></img></a>
<br></br>

[![python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![jupyter](https://img.shields.io/badge/Jupyter-Lab-F37626.svg?style=flat&logo=Jupyter)](https://jupyterlab.readthedocs.io/en/stable)
[![tensorflow](https://img.shields.io/badge/TensorFlow-1.12-FF6F00.svg?style=flat&logo=tensorflow)](https://www.tensorflow.org)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![pydocstyle](https://img.shields.io/badge/pydocstyle-enabled-AD4CD3)](http://www.pydocstyle.org/en/stable/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub release](https://img.shields.io/github/tag/pingcap/tidb.svg?label=release)](https://github.com/pingcap/aixpertlab/releases)
[![GitHub release date](https://img.shields.io/github/release-date/pingcap/tidb.svg)](https://github.com/pingcap/aixpertlab/releases)
 
[![Official Website](<https://img.shields.io/badge/-Visit%20the%20Official%20Website%20%E2%86%92-rgb(21,204,116)?style=for-the-badge>)](https://hypech.com)

[![jhc github](https://img.shields.io/badge/GitHub-aiXpertLab-181717.svg?style=flat&logo=github)](https://github.com/aiXpertLab)
[![jhc linkedin](https://img.shields.io/badge/Linkedin-aiXpert-5087B2.svg?style=flat&logo=Linkedin)](https://www.linkedin.com/in/aiXpert)
[![jhc twitter](https://img.shields.io/badge/Twitter-@aiXpertLab-00aced.svg?style=flat&logo=twitter)](https://twitter.com/aiXpertLab)
[![jhc fb](https://img.shields.io/badge/Facebook-aiXpertLab-5087B2.svg?style=flat&logo=facebook)](https://www.facebook.com/aiXpertLab/)
[![jhc gmail](https://img.shields.io/badge/Gmail-aiXpertLab@gmail.com-5087B2.svg?style=flat&logo=gmail)](https://gmail.com)

</div> 

# Overview

The AI-powered solution enables customers to integrate their specialized knowledge with OpenAI models to automate the extraction of relevant information from websites of their interest, effectively training the AI to deliver tailored results as if it were trained on their unique dataset.

- [GPT-4 from OpenAI](#architecture)
- [Powered by Python](#architecture)
- [Intuitive User Interface](#architecture)

You will get Unlock Your Personalized AI Assistant Effortlessly: Scrape, Upload, and Go.

# Project Overview

Why use Selenium in this project?
There are a few other common web scraping tools such as Beautifulsoup, Selenium, and Scrapy. Each of these tools has its advantages and disadvantages from different aspects although they have the same goal in the end.

In this project, we will be using Selenium which will help us to navigate between pages, fill out forms (such as login credentials), click links, etc. Briefly, besides the data scraping part, Selenium is going to be used to automate the following steps mentioned below to manage some actions until we access the pages where we will scrape the data. We will scrape the job offers and scrape their information by visiting 14 pages with each page having 25 job offers.



# Requirements:

1. Python experience (at least the first 15 days of this project).
2. Selenium & chromedriver installed (watch how in this one).
https://chromedriver.chromium.org/


# Quick start

1. 请首先配置好 openai 的 api（使用.env文件或者在代码中配置）
2. 将pdf简历上传到文件夹 auto_job_find 里，命名为 **“my_cover.pdf"**
3. 将需要的包安装好
4. 执行 write_response.py

## 关于 asistant

会自动生成 openai 的 asistant，并在本地产生一个 .json 文件，只有第一次运行的时候才会产生，后面每次运行如果检测到这个 json ，就会调用已有的 asistant。

## 使用到的包

- `python-dotenv`
- `openai`
- `selenium`
- `robotframework`
- `robotframework-seleniumlibrary`
- `robotframework-pythonlibcore`
- `faiss-cpu不支持3.12（faiss-gpu不清楚）。建议大家用3.11及以下版本的python运行脚本。` from @[huanmit](https://github.com/huanmit)

## About RPA

tutorial video about how to learn [rpa](https://www.youtube.com/watch?v=65OPFmEgCbM&list=PLx4LEkEdFArgrdD_lvXe_hYBy8zM0Sp3b&index=1)

Plugin: Intellibot@Selenium Library

------------------下面是简单的教学视频---------------------

[B站链接](https://www.bilibili.com/video/BV1UC4y1N78v/?share_source=copy_web&vd_source=b2608434484091fcc64d4eb85233122d)

[油管链接](https://youtu.be/TlnytEi2lD8?si=jfcDj2MZqBptziZc)

## 运行方式
先将该项目clone到本地，然后在项目根目录下执行
```bash
pip install -r requirements.txt
```

### assistant方式运行
打开.env文件，在里面配置好OpenAI的API key
随后将pdf简历上传到文件夹auto_job_find里，命名为“my_cover".随后执行write_response.py即可
这种方式不支持使用自定义api，优势是执行速度更快
如果需要使用自定义api，请使用下面的方式运行

### langchain方式
同样打开.env文件，在里面配置好OpenAI的API key和你想要请求的api地址
随后将pdf简历放到文件夹resume里
最后执行write_response.py即可

------------下面是其他朋友基于js构建的更加易于使用的代码---------------

我一直也在考虑如何可以降低各位的使用门槛，基于现在项目的热度，我发现很多朋友都需要这个东西来帮助自己，但是我相信对于更多的人而言，甚至vpn都是一个障碍

下面这位朋友基于js实现了一个更加简易的版本，虽然因为调用的免费api，无法使用assistant进行retrival，需要自己对简历进行简单的处理，但我依然认为这是个很棒的项目

感谢朋友的贡献，以下是链接：

[https://github.com/noBaldAaa](https://github.com/noBaldAaa/find-job)https://github.com/noBaldAaa/find-job

------------下面是其他朋友基于azure的openai api构建的版本的更加易于使用的代码---------------
https://github.com/LouisCaixuran/auto_job_find_azure




### Start with TiDB Cloud

TiDB Cloud is the fully-managed service of TiDB, currently available on AWS and GCP.

Quickly check out TiDB Cloud with [a free trial](https://tidbcloud.com/free-trial).

See [TiDB Cloud Quick Start Guide](https://docs.pingcap.com/tidbcloud/tidb-cloud-quickstart).

### Start with TiDB

See [TiDB Quick Start Guide](https://docs.pingcap.com/tidb/stable/quick-start-with-tidb).

### Start developing TiDB

See the [Get Started](https://pingcap.github.io/tidb-dev-guide/get-started/introduction.html) chapter of [TiDB Development Guide](https://pingcap.github.io/tidb-dev-guide/index.html).

## Community

You can join the following groups or channels to discuss or ask questions about TiDB, and to keep yourself informed of the latest TiDB updates:

- Seek help when you use TiDB
  - TiDB Forum: [English](https://ask.pingcap.com/), [Chinese](https://asktug.com)
  - [Discord](https://discord.gg/KVRZBR2DrG?utm_source=github)
  - Slack channels: [#everyone](https://slack.tidb.io/invite?team=tidb-community&channel=everyone&ref=pingcap-tidb) (English), [#tidb-japan](https://slack.tidb.io/invite?team=tidb-community&channel=tidb-japan&ref=github-tidb) (Japanese)
  - [Stack Overflow](https://stackoverflow.com/questions/tagged/tidb) (questions tagged with #tidb)
- Discuss TiDB's implementation and design
  - [TiDB Internals forum](https://internals.tidb.io/)
- Get the latest TiDB news or updates
    - Follow [@PingCAP](https://twitter.com/PingCAP) on Twitter
    - Read the PingCAP [English Blog](https://www.pingcap.com/blog/?from=en) or [Chinese Blog](https://cn.pingcap.com/blog/)

For support, please contact [PingCAP](http://bit.ly/contact_us_via_github).

## Contributing

The [community repository](https://github.com/pingcap/community) hosts all information about the TiDB community, including [how to contribute](https://github.com/pingcap/community/blob/master/contributors/README.md) to TiDB, how the TiDB community is governed, how [teams](https://github.com/pingcap/community/blob/master/teams/README.md) are organized.

Contributions are welcomed and greatly appreciated. You can get started with one of the [good first issues](https://github.com/pingcap/tidb/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) or [help wanted issues](https://github.com/pingcap/tidb/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22). For more details on typical contribution workflows, see [Contribute to TiDB](https://pingcap.github.io/tidb-dev-guide/contribute-to-tidb/introduction.html). For more contributing information about where to start, click the contributor icon below.

[<img src="docs/contribution-map.png" alt="contribution-map" width="180">](https://github.com/pingcap/tidb-map/blob/master/maps/contribution-map.md#tidb-is-an-open-source-distributed-htap-database-compatible-with-the-mysql-protocol)

Every contributor is welcome to claim your contribution swag by filling in and submitting this [form](https://forms.pingcap.com/f/tidb-contribution-swag).

<a href="https://next.ossinsight.io/widgets/official/compose-activity-trends?repo_id=41986369" target="_blank" style="display: block" align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://next.ossinsight.io/widgets/official/compose-activity-trends/thumbnail.png?repo_id=41986369&image_size=auto&color_scheme=dark" width="822" height="auto">
    <img alt="Activity Trends of pingcap/tidb - Last 28 days" src="https://next.ossinsight.io/widgets/official/compose-activity-trends/thumbnail.png?repo_id=41986369&image_size=auto&color_scheme=light" width="822" height="auto">
  </picture>
</a>

## Case studies

- [Case studies in English](https://www.pingcap.com/customers/)
- [中文用户案例](https://cn.pingcap.com/case/)

## Architecture

![TiDB architecture](./docs/tidb-architecture.png)

## License

TiDB is under the Apache 2.0 license. See the [LICENSE](./LICENSE) file for details.

## Acknowledgments

- Thanks [cznic](https://github.com/cznic) for providing some great open source tools.
- Thanks [GolevelDB](https://github.com/syndtr/goleveldb), [BoltDB](https://github.com/boltdb/bolt), and [RocksDB](https://github.com/facebook/rocksdb) for their powerful storage engines.

First, I do not condone scraping LinkedIn data in any way. Anyone who wishes to do so should first read LinkedIn's statement on their prohibition of scraping software.https://www.linkedin.com/help/linkedin/answer/a1341387/prohibition-of-scraping-software?lang=en
Warning: LinkedIn has strong anti-scraping policies, they may blacklist ips making unauthenticated or unusual requests

What's Inside?
In this project, I have used Selenium library to automate the scraping process, navigate between pages, fill out forms (such as login credentials), click links, etc. Briefly, besides the data scraping part, Selenium was used to automate the following steps mentioned below to manage some actions until we access the pages where we will scrape the data. I have scraped the job offers and scraped their information by visiting 14 pages with each page having 25 job offers.

Automated Steps

Enter to Linkedin login page
Spot the cookies pop-up and click Accept cookies
Fill E-Mail Address and Password areas and click Login 
Click on the Jobs from the section above 
Search for job positions Junior Data Analyst in Spain
Scroll down till the end of the page while collecting the link of each displayed Job offer
Go to the next page when it is the end of the page while keep collecting links 
After all links are collected, go to the each link
Click the "See More" button the expand the job description text.
Scrape the desired data 
Items Scraped:

Job Title
Company Name
Company Location
Job Description
Work Method (Hybrid, Remote, On-Site)
Experience Level
Post Date
Extra:

You can check my medium post where I have analyzed the d

https://selenium-python.readthedocs.io/