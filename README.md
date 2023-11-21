# PsychoPy

## Sound

If using `pyo`, you may require additional system dependencies. On a Mac, you can install these using Homebrew. If you don't have Homebrew installed, you can install it from <https://brew.sh/>.

Once Homebrew is installed, you can install the necessary dependencies. Common dependencies for audio processing include:

```bash
brew install portaudio
brew install libsndfile
```

`portaudio` is used for audio I/O.

`libsndfile` is used for reading and writing audio files.

## EyeLink

You’ll need to download the Eyelink Developers Kit provided by SR Research. To do that, register an account [here](https://www.sr-support.com/).

Note that they moderate the accounts fairly heavily, so it may take 24 hrs+ for the registration to go though. Once you’re registered, you can download the developers kit API ( Windows, Linux, MacOS ). You’ll need that kit to be able to call Eyelink functions from within PsychoPy (otherwise you get an error about missing files). Registering also gives access to a support forum.

The link to the download page, once you have access:
<https://www.sr-research.com/support/thread-13.html>
