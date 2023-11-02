package com.example.temp_backend.controller;

import com.example.temp_backend.Services.UserLoginService;
import com.example.temp_backend.model.User;
import com.example.temp_backend.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping(path = "/user")
public class UserController {

    @Autowired
    UserRepository userRepository;

    @Autowired
    UserLoginService userService;

    @GetMapping(path = "/all")
    public @ResponseBody Iterable<User> getAllUser() {
        return userRepository.findAll();
    }
    @GetMapping(path = "/{id}")
    public @ResponseBody Optional<User> getUserById(@PathVariable Long id) {
        return userRepository.findById(id);
    }

    @PostMapping
    User insertUser(@RequestBody User newUser) throws Exception {
        return userService.registerNewUser(newUser);
    }

    @PutMapping("/{id}")
    User replaceUser(@RequestBody User newUser, @PathVariable Long id) {

        return userRepository.findById(id)
                .map(User -> {
                    User.setUsername(newUser.getUsername());
                    User.setPassword(newUser.getPassword());
                    User.setAdmin(newUser.isAdmin());
                    User.setPhoneNumber(newUser.getPhoneNumber());
                    User.setLoginTries(newUser.getLoginTries());
                    User.setFirstName(newUser.getFirstName());
                    User.setLastName(newUser.getLastName());
                    return userRepository.save(User);
                })
                .orElseGet(() -> {
                    newUser.setId(id);
                    return userRepository.save(newUser);
                });
    }

    @DeleteMapping("/{id}")
    void deleteUser(@PathVariable Long id) {
        userRepository.deleteById(id);
    }
}