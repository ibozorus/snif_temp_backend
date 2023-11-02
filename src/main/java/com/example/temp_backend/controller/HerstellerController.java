package com.example.temp_backend.controller;

import com.example.temp_backend.model.Hersteller;
import com.example.temp_backend.repository.HerstellerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "/hersteller")
public class HerstellerController {

    @Autowired
    HerstellerRepository herstellerRepository;

    @GetMapping(path = "/all")
    public @ResponseBody Iterable<Hersteller> getAllHersteller() {
        return herstellerRepository.findAll();
    }

}
