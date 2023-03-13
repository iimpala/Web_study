package hellojpa;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;
import java.util.List;

public class JpaMain {
    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();

        EntityTransaction tx = em.getTransaction();
        tx.begin();

        try {
//            //생성
//            Member member = new Member();
//            member.setId(2L);
//            member.setName("HelloB");
//            em.persist(member);

//            //조회
//            Member findMember = em.find(Member.class, 1L);

//            //삭제
//            em.remove(findMember)

//            //수정
//            findMember.setName("HelloJPA");

//            //jpql
//            List<Member> result = em.createQuery("select m from Member m", Member.class)
//                    .setFirstResult(1) //1번부터
//                    .setMaxResults(10) //10개 가져와
//                    .getResultList();
//            for (Member member : result) {
//                System.out.println("member = " + member.getName());
//            }

//            //영속성 컨텍스트
//            //비영속
//            Member member = new Member();
//            member.setId(101L);
//            member.setName("HelloJPA");
//
//            //영속
//            System.out.println("=== BEFORE ===");
//            em.persist(member); //DB에 저장 X(INSERT 쿼리 전송X)
//            System.out.println("=== AFTER ===");

//            //1차캐시
//            Member findMember1 = em.find(Member.class, 101L); //DB에서 조회, 1차캐시에 저장
//            Member findMember2 = em.find(Member.class, 101L); //1차캐시에서 조회
//            System.out.println("findMember1 = " + findMember1.getName());
//            System.out.println("findMember2 = " + findMember2.getName());
//
//            System.out.println("result = " + (findMember1 == findMember2));

//            //준영속
//            em.detach(member);
//            em.clear();
//            em.close();
//
//            //삭제
//            em.remove(member);

//            //쓰기 지연
//            Member member1 = new Member(150L, "A");
//            Member member2 = new Member(160L, "B");
//
//            em.persist(member1);
//            em.persist(member2);
//
//            System.out.println("==========================");

//            //변경감지
//            Member member = em.find(Member.class, 150L);
//            member.setName("Z"); // 자바 컬렉션 다루듯이 값만 변경하면 자동으로 DB에 반영
//
//            System.out.println("==========================");

//            //플러시
//            Member member = new Member(200L, "member200");
//            em.persist(member);
//            em.flush(); //변경사항 반영
//            System.out.println("==========================");

            //쓰기 지연
            tx.commit(); //DB에 저장 O(INSERT 쿼리 전송)
        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }

        emf.close();
    }
}
