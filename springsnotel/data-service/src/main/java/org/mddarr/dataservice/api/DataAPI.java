package org.mddarr.dataservice.api;

import org.mddarr.dataservice.entity.LocationEntity;
import org.mddarr.dataservice.services.DataService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.List;


@RestController
@RequestMapping(value = "/data/")
@CrossOrigin
public class DataAPI {

    @Autowired
    private DataService dataService;

    @GetMapping()
    public String get() throws IOException {
        return "hello";
    }


    @GetMapping(value = "/location/")
    public List<LocationEntity> getLocations() throws IOException {
        return dataService.getLocations();
    }

//
//    @GetMapping(value = "/location/")
//    public List<LocationEntity> getTimeSeries(@RequestParam(value="id") String id, @RequestParam(value="") String name) throws IOException {
//        return dataService.getLocations();
//    }



}
