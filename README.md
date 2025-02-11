# Framework Performance Testing

[![Become a sponsor to ADernild](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/ADernild "Become a sponsor to ADernild")
[![GitHub](https://img.shields.io/github/followers/adernild?label=follow&style=social)](https://github.com/ADernild "Follow ADernild on GitHub")
[![Docker](https://img.shields.io/badge/Docker-white?style=flat-round&logo=docker&logoColor=#1D63ED)](https://hub.docker.com/u/adernild "Follow ADernild on Docker Hub")
[![LinkedIn](https://img.shields.io/badge/-Alexander_Dernild-blue?style=flat-round&logo=Linkedin&logoColor=white&link=https://linkedin.com/in/alexander-dernild)](https://linkedin.com/in/alexander-dernild "Connect with me on LinkedIn")
[![E-Mail](https://img.shields.io/badge/E_mail-8B89CC?style=flat-round&logo=protonmail&logoColor=white)](mailto:alex@dernild.dk)
[![Akami Cloud Computing](https://img.shields.io/badge/Cloud_Hosting-s?style=flat-round&logo=akamai&logoColor=%230096D6&labelColor=white&color=white)](https://www.linode.com/lp/refer/?r=a1236b8e74912ccb090628165fa6bf21cb52968f "Get a $100 credit on Linode Cloud")


This repository contains scripts to test and compare the performance of different web frameworks using `wrk` (a modern HTTP benchmarking tool) and Docker stats for resource usage monitoring. The results are stored in text files within the `/logs` directory.

## Table of Contents

- [Frameworks Tested](#frameworks-tested)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Tests](#running-the-tests)
- [Results](#results)

## Frameworks Tested

The following frameworks are tested in this project:

1. **Django** (both synchronous and asynchronous endpoints)
2. **FastAPI** (both synchronous and asynchronous endpoints)
3. **Actix Web** (both synchronous and asynchronous endpoints)

## Prerequisites

Before running the tests, ensure you have the following installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [wrk](https://github.com/wg/wrk)
- Python 3.13

## Setup

1. **Clone the Repository**

   ```sh
   git clone https://github.com/adernild/framework-performance-testing.git
   cd framework-performance-testing
   ```
2. **Build and Run Docker Containers**

   Run the containers:

      ```sh
      docker-compose up -d
      ```

## Running the Tests

1. **Ensure Docker Containers Are Running**

   Make sure all the necessary Docker containers are up and running:

   ```sh
   docker ps
   ```

2. **Run the Test Script**

   Navigate to the directory containing the test script and run it:

   ```sh
   cd framework-test/test
   python test_api.py
   ```

   This script will:
   - Run `wrk` tests on each endpoint.
   - Capture Docker stats for CPU and memory usage during the tests.
   - Store the results in text files within the `/logs` directory.

## Results

After running the tests, you will find several `.txt` log files in the `/logs` directory. Each file contains the output from `wrk` and Docker stats for a specific framework and endpoint.

Example of log files:

- `framework-test-django-1_sleep-async_wrk_output.txt`
- `framework-test-django-1_sleep-sync_wrk_output.txt`
- `framework-test-fastapi-1_sleep-async_wrk_output.txt`
- `framework-test-fastapi-1_sleep-sync_wrk_output.txt`
- `framework-test-actix_web-1_sleep-async_wrk_output.txt`
- `framework-test-actix_web-1_sleep-sync_wrk_output.txt`

These files provide detailed performance metrics for each framework and endpoint, including the output from `wrk` and Docker stats.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to improve this project.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
