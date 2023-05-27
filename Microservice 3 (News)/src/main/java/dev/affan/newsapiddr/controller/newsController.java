package dev.affan.newsapiddr.controller;

import dev.affan.newsapiddr.entity.Article;
import dev.affan.newsapiddr.service.newsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/news")
public class newsController {

    @Autowired
    private newsService newsservice;

    @GetMapping("/")
    public ResponseEntity<List<Article>> getAllNews(){
        List<Article> news = this.newsservice.getAllNews();
        return new ResponseEntity<List<Article>>(news, HttpStatus.OK);
    }
}
