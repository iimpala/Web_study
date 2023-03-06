package jpabook.jpashop.service;

import jpabook.jpashop.domain.item.Book;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import javax.persistence.EntityManager;

@RunWith(SpringRunner.class)
@SpringBootTest
public class ItemUpdateTest {

    @Autowired
    EntityManager em;

    @Test
    public void updateTest() {
        Book book = em.find(Book.class, 1L);

        //TX
        book.setName("adsfa");

        //변경감지 == dirty checking
        //DB에 업데이트 쿼리를 보내지 않아도 트랜잭션 커밋 시점에 jpa가 변경을 감지해서 DB에 반영
        //TX commit

    }
}
