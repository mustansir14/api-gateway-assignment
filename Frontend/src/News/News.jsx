import { useState, useEffect } from "react";
import "./News.css";

export default function News() {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`http://localhost:8000/news`, {
      method: "GET",
      credentials: "include",
      headers: {
        Accept: "application/json",
        "Access-Control-Allow-Origin": "http://localhost:3000/",
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        if (response) return response.json();
      })
      .then((data) => {
        setNews(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching news:", error);
        setLoading(false);
      });
  }, []);

  return (
    <div className="news">
      <h1>Top News for today</h1>
      <div className="innercontainer">
        {loading ? (
          <div className="article">Loading...</div>
        ) : (
          news.map((article, index) => (
            <div className="article">
              <a href={article.url}>{`${index + 1}. ${article.title}`}</a>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
