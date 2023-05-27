package dev.affan.newsapiddr.service;

import dev.affan.newsapiddr.entity.Article;
import dev.affan.newsapiddr.entity.News;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.List;

@Service
public class newsService {

    @Autowired
    private RestTemplate restTemplate;

    private String url = "https://newsapi.org/v2/top-headlines?country=us&pageSize=10&apiKey=7bbadccb5a434432bb968e6bfb0de346";

    public List<Article> getAllNews(){
        return restTemplate.getForObject(url, News.class).articles;
    }

}
