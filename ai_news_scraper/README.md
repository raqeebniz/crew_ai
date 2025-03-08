# 📰 AI News Scraper  

An AI-powered news scraper that fetches news articles on a user-provided topic and saves the data to a file. It utilizes **CrewAI** to coordinate agents, tasks, and tools for efficient web scraping.  

## 🚀 Features  
- Scrapes news articles based on user input  
- Uses **CrewAI** for agent-based task execution  
- Saves scraped data to a file for easy access  

## 🛠️ Technologies Used  
- **Python**  
- **CrewAI** (Agents, Tasks, Crews, and Tools)  
- **UV** (for efficient execution)  

## 📂 Project Structure  
```
AI_NEWS_SCRAPER/
│── .venv/                  # Virtual environment  
│── knowledge/              # Stores knowledge files  
│── news/                   # Scraped news data  
│── src/ai_news_scraper/    # Main source code  
│   │── _pycache_/          # Python cache  
│   │── config/             # Configuration files  
│   │── tools/              # Custom tools for scraping  
│   │── __init__.py         # Package initializer  
│   │── crew.py             # CrewAI setup (agents, tasks, crews)  
│   │── main.py             # Entry point of the scraper  
│── tests/                  # Test cases  
│── .env                    # Environment variables  
│── .gitignore              # Git ignore file  
│── output.md               # Output file for scraped data  
│── pyproject.toml          # Project dependencies  
│── README.md               # Documentation  
│── uv.lock                 # Lockfile for dependencies  
```

## ⚡ How to Use  
1. Install dependencies:  
   ```bash
   pip install crewai uv
   ```  
2. Run the scraper:  
   ```bash
   python main.py
   ```  
3. Enter a topic when prompted, and the scraped data will be saved automatically in the `news/` directory.  

## 🎯 Contribution  
Feel free to contribute by improving the scraper, adding more features, or optimizing performance. Fork the repository, make your changes, and submit a pull request.  

Happy coding! 🚀  
