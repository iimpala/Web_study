package hello.core.web;


import hello.core.common.MyLogger;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class LogDemoService {

    @Autowired
    public LogDemoService(MyLogger myLogger) {
        this.myLogger = myLogger;
        System.out.println("[LogDemoService - Constructor] myLogger = " + myLogger.getClass());
    }

    private final MyLogger myLogger;

    public void logic(String id) {
        System.out.println("[LogDemoService] myLogger = " + myLogger.getClass());
        myLogger.log("service id = " + id);
    }
}
