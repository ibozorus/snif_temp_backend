package com.example.temp_backend.controller;

import com.example.temp_backend.model.ServerCabin;
import com.example.temp_backend.repository.ServerCabinRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping(path = "/servercabin")
public class ServerCabinController {


    @Autowired
    ServerCabinRepository serverCabinRepository;


    @GetMapping(path = "/all")
    public @ResponseBody Iterable<ServerCabin> getAllServerCabin() {
        return serverCabinRepository.findAll();
    }

    @GetMapping(path = "/{id}")
    public @ResponseBody Optional<ServerCabin> getServerCabinById(@PathVariable Long id) {
        return serverCabinRepository.findById(id);
    }

    @PostMapping
    ServerCabin insertHersteller(@RequestBody ServerCabin newServerCabin) {
        return serverCabinRepository.save(newServerCabin);
    }

    @PutMapping("/{id}")
    ServerCabin replaceServerCabin(@RequestBody ServerCabin newServerCabin, @PathVariable Long id) {

        return serverCabinRepository.findById(id)
                .map(ServerCabin -> {
                    ServerCabin.setFloor(newServerCabin.getFloor());
                    return serverCabinRepository.save(ServerCabin);
                })
                .orElseGet(() -> {
                    newServerCabin.setId(id);
                    return serverCabinRepository.save(newServerCabin);
                });
    }

    @DeleteMapping("/{id}")
    void deleteServerCabin(@PathVariable Long id) {
        serverCabinRepository.deleteById(id);
    }

}
