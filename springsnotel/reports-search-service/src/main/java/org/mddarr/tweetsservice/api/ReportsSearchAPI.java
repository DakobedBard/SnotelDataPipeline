package org.mddarr.tweetsservice.api;

import org.apache.lucene.queryparser.flexible.core.builders.QueryBuilder;
import org.elasticsearch.ElasticsearchException;
import org.elasticsearch.action.admin.indices.create.CreateIndexRequest;
import org.elasticsearch.action.admin.indices.create.CreateIndexResponse;
import org.elasticsearch.action.get.GetRequest;
import org.elasticsearch.action.get.GetResponse;
import org.elasticsearch.action.index.IndexRequest;
import org.elasticsearch.action.index.IndexResponse;
import org.elasticsearch.action.search.SearchRequest;
import org.elasticsearch.action.search.SearchResponse;
import org.elasticsearch.action.search.SearchType;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.common.unit.Fuzziness;
import org.elasticsearch.index.query.QueryBuilders;
import org.elasticsearch.rest.RestStatus;
import org.elasticsearch.search.builder.SearchSourceBuilder;
import org.mddarr.tweetsservice.dao.ArticleRepository;
import org.mddarr.tweetsservice.model.Article;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.elasticsearch.core.ElasticsearchOperations;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping(value = "/article/")
public class ReportsSearchAPI {

    @Autowired
    RestHighLevelClient highLevelClient;

    public String getTweets(RestHighLevelClient client, String indexName) throws IOException {
        System.out.println("Whatttt");
        SearchRequest searchRequest = new SearchRequest();
        SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
        searchSourceBuilder.query(QueryBuilders.matchAllQuery());
        searchRequest.source(searchSourceBuilder);
        SearchResponse response = client.search(searchRequest,RequestOptions.DEFAULT);
        return response.toString();
    }



    public String getArticle(RestHighLevelClient client, String indexName) throws IOException {

//        SearchRequest searchRequest = new SearchRequest();
//        SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
//        searchSourceBuilder.query(QueryBuilders.matchAllQuery());
//        searchRequest.source(searchSourceBuilder);

        GetRequest request = new GetRequest("articlesindex","_doc", "1");
        try {
            GetResponse getResponse = client.get(request, RequestOptions.DEFAULT);
            System.out.println("response " + getResponse.toString());
            return getResponse.toString();
        } catch (ElasticsearchException e) {
            if (e.status() == RestStatus.NOT_FOUND) {
            }
        }
        return "df";
    }

    @GetMapping(value="get")
    public String get() throws IOException {
//        String resposne = this.getArticle(this.highLevelClient, "articlesindex");
        String response = this.getTweets(this.highLevelClient, "Hello");
        return response;
    }

//    @GetMapping(value="get")
//    public String searchTweets() throws IOException {
//        String resposne = this.getArticle(this.highLevelClient, "articlesindex");
//        return resposne;
//    }



    public boolean addDocumentIndex(RestHighLevelClient client, String indexName) throws IOException {
        Map<String, Object> jsonMap = new HashMap<>();
        jsonMap.put("dumb", "stupid");

        jsonMap.put("postDate", new Date());
        jsonMap.put("message", "trying out Elasticsearch");
        IndexRequest indexRequest = new IndexRequest("articlesindex").type("_doc")
                .id("2").source(jsonMap);
        IndexResponse indexResponse = client.index(indexRequest, RequestOptions.DEFAULT);
        return true;
    }

    public boolean createIndex(RestHighLevelClient client, String indexName) throws IOException {
        CreateIndexRequest request = new CreateIndexRequest(indexName);
        //no options just straight forward
        CreateIndexResponse response = client.indices().create(request, RequestOptions.DEFAULT);
        return response.isAcknowledged();
    }

    @GetMapping
    public String postTweet() throws IOException {
        this.addDocumentIndex(this.highLevelClient, "articlesindex");
        return "create index";
    }

    @GetMapping(value = "create/")
    public String getTweets() throws IOException {
        this.createIndex(highLevelClient, "articlesindex");
        return "create index";
    }
}
