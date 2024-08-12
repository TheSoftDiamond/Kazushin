<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/thesoftdiamond/Kazushin">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Kazushin</h3>

  <p align="center">
    Kazushin, a fork of <a href="https://github.com/adi-panda/Kuebiko">this project</a>, is a Twitch Chat Bot that reads chat and generates text-to-speech responses using OpenAI API and Google Cloud API. It comes with profanity detection, and more built-in.
    <br />
    <a href="https://docs.kazush.in/en/home"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/TheSoftDiamond/Kazushin/">View Demo</a>
    ·
    <a href="https://github.com/TheSoftDiamond/Kazushin/issues">Report Bug</a>
    ·
    <a href="https://github.com/TheSoftDiamond/Kazushin/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

<!-- GETTING STARTED -->
## Getting Started

For a more comprehensive guide, [check out the documentation](https://docs.kazush.in/en/home)

### Prerequisites
- [Ollama](https://ollama.com/download)
- [VLC](https://www.videolan.org/vlc/)
- [Python 3.12.0](https://www.python.org/downloads/release/python-3120/)

In order to install the prerequisites, you will need to run the following command in a command line:  
* pip
  ```sh
  pip install -r requirements.txt
  ```

### Installation

1. Clone the repo or fork it
   ```sh
   git clone https://github.com/TheSoftDiamond/Kazushin.git
   ```
2. Populate the creds.py file with your info
3. Adjust the settings.py file as to your needs.
4. Run main_usercontext.py

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Setting up Ollama
Make sure you have downloaded [Ollama](https://ollama.com/download).
#### Creating the model
1. Create a `Modelfile` in your project, pointing it to your model gguf:
    ```
    FROM llama-2-7b.Q2_K.gguf
    ```
    *You can download model data from sites such as [HuggingFace](https://huggingface.co/models)*
2. Create the Ollama model from your existing template using poweshell/bash
    ```bash
    ❯ ollama create llama2 -f Modelfile
    transferring model data 
    creating model layer 
    using already created layer sha256:a630f354771cf25496e079a49656730858712315cc71aee4adf9b97aceb251f8 
    writing layer sha256:9d07cddc325f2abd269514a29cb3165eac0b06accd018a1b4da9982d6b986647 
    writing manifest 
    success
    ```
3. Serve the Ollama instance
    ```bash
    ❯ ollama serve
    time=2024-07-10T20:20:46.364-04:00 level=INFO source=images.go:710 msg="total blobs: 0"
    time=2024-07-10T20:20:46.364-04:00 level=INFO source=images.go:717 msg="total unused blobs removed: 0"
    time=2024-07-10T20:20:46.364-04:00 level=INFO source=routes.go:1021 msg="Listening on 127.0.0.1:11434 (version 0.1.28)"
    time=2024-07-10T20:20:46.364-04:00 level=INFO source=payload_common.go:107 msg="Extracting dynamic libraries..."
    time=2024-07-10T20:20:47.967-04:00 level=INFO source=payload_common.go:146 msg="Dynamic LLM libraries [rocm_v5 cpu_avx2 cpu rocm_v6 cpu_avx cuda_v11]"
    time=2024-07-10T20:20:47.967-04:00 level=INFO source=gpu.go:94 msg="Detecting GPU type"
    time=2024-07-10T20:20:47.967-04:00 level=INFO source=gpu.go:265 msg="Searching for GPU management library libnvidia-ml.so"
    time=2024-07-10T20:20:47.980-04:00 level=INFO source=gpu.go:311 msg="Discovered GPU libraries: []"
    time=2024-07-10T20:20:47.980-04:00 level=INFO source=gpu.go:265 msg="Searching for GPU management library librocm_smi64.so"
    time=2024-07-10T20:20:47.980-04:00 level=INFO source=gpu.go:311 msg="Discovered GPU libraries: []"
    time=2024-07-10T20:20:47.980-04:00 level=INFO source=cpu_common.go:11 msg="CPU has AVX2"
    time=2024-07-10T20:20:47.980-04:00 level=INFO source=routes.go:1044 msg="no GPU detected"
    ```
    This is foreground process, you will need to have this as a service in order to utilize it as a daemon.
    
    For example, on Linux systems: `systemctl enable --now ollama`.
    This will enable Ollama on boot.

4.  In settings.py adjust the `localAI_ModelName` to match your model name.
    ```python
    ### Local AI SETTINGS ###
    # Model Name
    localAI_ModelName = "llama2"
    ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FEATURES -->
## Features
* Separate conversations, prompts per user.
* Profanity Filter
* Detect Cheers, Keywords, andmore
* Have the bot speak out loud or/and post messages to chat
* [and many more!](https://docs.kazush.in/en/install/features)

## Usage

[See here](https://docs.kazush.in/en/home)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Profanity Filter, by arhankundu99](https://github.com/arhankundu99/profanity-filter)
* [Kuebiko, by adi-panda](https://github.com/adi-panda/Kuebiko)
* [twitch_chat, by MariusPerle](https://github.com/MariusPerle/twitch_chat)
* [Ollama, by Ollama](https://github.com/ollama/ollama)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/thesoftdiamond/kazushin/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/thesoftdiamond/kazushin.svg?style=for-the-badge
[forks-url]: https://github.com/thesoftdiamond/kazushin/network/members
[stars-shield]: https://img.shields.io/github/stars/thesoftdiamond/kazushin.svg?style=for-the-badge
[stars-url]: https://github.com/thesoftdiamond/kazushin/stargazers
[issues-shield]: https://img.shields.io/github/issues/thesoftdiamond/kazushin.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.webp
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
