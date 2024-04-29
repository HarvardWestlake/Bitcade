# Bitcade: The Decentralized Arcade Platform

Welcome to **Bitcade**, the fully decentralized arcade platform where game logic is powered by blockchain technology. Bitcade uses the [Ape Framework](https://docs.apeworx.io/ape/stable/) and is developed in Vyper, providing a secure and developer-friendly environment for building and deploying games.

## Features

- **Blockchain-based**: All game logic is on-chain for verifiable fairness and transparency.
- **Developer Incentives**: Developers can build front-facing applications and receive a percentage of arcade tickets distributed, promoting a collaborative and rewarding ecosystem.
- **Dynamic Game Library**: Launching with popular titles such as **Crash** and **Blinko**, with plans to expand the library continually.

## Getting Started

### Prerequisites

Before starting, ensure you have installed:
- [Python 3.7+](https://www.python.org/downloads/)
- [Ape Framework](https://docs.apeworx.io/ape/stable/userguides/quickstart.html)

### Installation

Clone the repository to get started:

```bash
git clone git@github.com:HarvardWestlake/Bitcade.git
cd Bitcade
ape test
```

### Development
- Create your feature branch: git checkout -b feature/YourFeatureName
- Commit your changes: git commit -m 'Add some feature'
- Push to the branch: git push origin feature/YourFeatureName
- Submit a pull request: We welcome all contributions and will review your pull request.
- Contributors whose games or apps significantly drive ticket distribution will earn a percentage of those tickets. Join us in building the future of decentralized arcade gaming!

## UI Testing
Playwright Test project inside the folder ui

https://playwright.dev/docs/intro#running-the-example-test-in-ui-mode

Inside that directory, you can run several commands:

  npx playwright test
    Runs the end-to-end tests.

  npx playwright test --ui
    Starts the interactive UI mode.

  npx playwright test --project=chromium
    Runs the tests only on Desktop Chrome.

  npx playwright test example
    Runs the tests in a specific file.

  npx playwright test --debug
    Runs the tests in debug mode.

  npx playwright codegen
    Auto generate tests with Codegen.

We suggest that you begin by typing:

    npx playwright test

And check out the following files:
  - .\ui\tests\example.spec.js - Example end-to-end test
  - .\ui\tests-examples\demo-todo-app.spec.js - Demo Todo App end-to-end tests
