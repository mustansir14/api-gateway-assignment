package dev.affan.newsapiddr.entity;

import lombok.Data;

import java.util.List;

@Data
public class News {
    public List<Article> articles;
}
