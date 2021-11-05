# AI-OpenMic

Code and Dataset repository for the EMNLP 2021 paper:

### [“So You Think You’re Funny?”: Rating the Humour Quotient in Standup Comedy](http://dipteshkanojia.github.io/publication/emnlp-2021-standup/).

* Paper: [Link](http://dipteshkanojia.github.io/files/emnlp-2021-standup.pdf)
* Poster: [Link](http://dipteshkanojia.github.io/files/poster-emnlp-2021-funny.pdf)
* Slides: [Link](http://dipteshkanojia.github.io/files/ppt-emnlp-2021-funny.pdf)
* Video: [Link](http://dipteshkanojia.github.io/files/video-emnlp-2021-standup.mp4)

## Dataset

The dataset is available for [download via the following link](https://www.cfilt.iitb.ac.in/~diptesh/AI_open_mic_dataset.zip).

## Code

The complete codebase shall be made available very soon. Thank you for being patient.

## Citing
Please use the following citation while citing this work:

```latex
@inproceedings{mittal-etal-2021-think,
    title = "{``}So You Think You{'}re Funny?{''}: Rating the Humour Quotient in Standup Comedy",
    author = "Mittal, Anirudh  and
      P, Pranav Jeevan  and
      Gandhi, Prerak  and
      Kanojia, Diptesh  and
      Bhattacharyya, Pushpak",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-main.789",
    pages = "10073--10079",
    abstract = "Computational Humour (CH) has attracted the interest of Natural Language Processing and Computational Linguistics communities. Creating datasets for automatic measurement of humour quotient is difficult due to multiple possible interpretations of the content. In this work, we create a multi-modal humour-annotated dataset ({\textasciitilde}40 hours) using stand-up comedy clips. We devise a novel scoring mechanism to annotate the training data with a humour quotient score using the audience{'}s laughter. The normalized duration (laughter duration divided by the clip duration) of laughter in each clip is used to compute this humour coefficient score on a five-point scale (0-4). This method of scoring is validated by comparing with manually annotated scores, wherein a quadratic weighted kappa of 0.6 is obtained. We use this dataset to train a model that provides a {`}funniness{'} score, on a five-point scale, given the audio and its corresponding text. We compare various neural language models for the task of humour-rating and achieve an accuracy of 0.813 in terms of Quadratic Weighted Kappa (QWK). Our {`}Open Mic{'} dataset is released for further research along with the code.",
}
```

