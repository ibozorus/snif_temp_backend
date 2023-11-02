package com.example.temp_backend.Services;

import com.example.temp_backend.repository.UserRepository;
import com.example.temp_backend.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Objects;

@Service
public class UserLoginService {

    @Autowired
    private UserRepository userRepository;

    public HashMap<String, String> checkLogin(long id, String password) {
        User user = userRepository.findById(id)
                .orElseThrow(() -> new IllegalStateException("User does not exist"));

        HashMap<String, String> response = new HashMap<>();

        String hashedPassword = hashPassword(password);

        if (Objects.equals(user.getPassword(), hashedPassword)) {
            response.put("message", "success");
            response.put("userId", user.getId().toString());
        } else {
            response.put("message", "fail");
        }
        return response;
    }

    public User registerNewUser(User user) throws Exception {
        Iterable<User> users = userRepository.findAll();

        for (User lUser:
             users) {
            if (user.getUsername().equals(lUser.getUsername()))
                throw  new Exception("Der Nutzername existiert bereits");
        }
        return userRepository.save(user);
    }

    private String hashPassword(String password) {
        String generatedPassword = null;

        try {
            MessageDigest md = MessageDigest.getInstance("MD5");

            md.update(password.getBytes());

            byte[] bytes = md.digest();

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < bytes.length; i++) {
                sb.append(Integer.toString((bytes[i] & 0xff) + 0x100, 16).substring(1));
            }

            // Get complete hashed password in hex format
            generatedPassword = sb.toString();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        return generatedPassword;
    }
}