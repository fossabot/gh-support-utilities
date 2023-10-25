---
name: Required Compliance Scan via FOSSA
about: The purpose of this issue template is to help you get started on compliance
  scans with FOSSA
title: 'Required OSS compliance scan'
labels: compliance-scan, fossa, open-source
assignees: ''

---

### Howdy! So, what's this about?
 
Our company is required to go through regular compliance scans of all open source projects. We use FOSSA as our software composition analysis tool to help with this. To understand what FOSSA is, please go through the following videos to get started:

#### What is FOSSA?

- [ ] https://www.youtube.com/watch?v=J13f6l5t1wc
- [ ] https://www.youtube.com/watch?v=0CzExe1L61E
- [ ] https://www.youtube.com/watch?v=uiuB63GtilA

#### FOSSA for Developers

- [ ] https://www.youtube.com/watch?v=yasx6Ji3yUs
- [ ] Using the FOSSA CLI: https://github.com/fossas/fossa-cli#getting-started


#### 101 FOSSA Videos

- [ ] Running your first scan: https://www.youtube.com/watch?v=27Xo4jIi1O0
- [ ] Understanding scan results: https://www.youtube.com/watch?v=94JWHqurXD4
- [ ] Resolving Issues: https://www.youtube.com/watch?v=9c0HzwtpUJg
- [ ] SBOMs: https://www.youtube.com/watch?v=H3UqVumgUFQ

#### Useful references to bookmark
- [ ] https://github.com/fossas/fossa-cli/tree/master#fossa-cli
- [ ] https://github.com/fossas/fossa-cli/tree/master/docs
- [ ] https://docs.fossa.com

### What do I do next?

OK! We require you to use the FOSSA CLI to integrate your OSS project. Please look for the FOSSA workflow template here. Make sure to set your FOSSA access token in your repository settings.

Report any integration issues to your OSS manager. If issues persist, please create a ticket by emailing  support@fossa.com with as many details as possible. `fossa analyze --debug` outputs a `fossa.debug.json.gz`. Please include that in your ticket, along with any useful screenshots.

If the scan is successful, please tag ___ in this issue to let them know the results are available for review.
