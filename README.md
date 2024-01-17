# haystack-rag-showcase

This project is a showcase for haystack's api 2.0, highlighting its pipeline. This project consists of a few parts:

1.  Scraping TUM CIT website with either scrapy (`scripts/TUM_RAG.ipynb`) or beautiful soup (`scripts/TUM_RAG_with_beautiful_soup.ipynb`)
2.  HTML text processing, chunking, and writing to different stores
3.  Retrieval-Augmented Question Answering system, which handles english and german input differently.

## Local setup with access to disk (more powerful)

### Get data

Go to tum_crawler with `cd tum_crawler`

In terminal, run `scrapy crawl tum` (might require installation)

### Process data

Go back to project root.

Run `docker-compose up` to run the qdrant databases.

Create .env at project root, with your token: `OAI_TOKEN="sk-..."`

Read & execute `scripts/TUM_RAG.ipynb`

## With Colab Only

Read & execute `scripts/TUM_RAG_with_beautiful_soup.ipynb`
