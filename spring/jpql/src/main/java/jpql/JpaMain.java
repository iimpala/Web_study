package jpql;

import javax.persistence.*;
import java.util.List;

public class JpaMain {

    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();

        EntityTransaction tx = em.getTransaction();
        tx.begin();

        try {
            Team teamA = new Team();
            teamA.setName("teamA");
            em.persist(teamA);

            Team teamB = new Team();
            teamB.setName("teamB");
            em.persist(teamB);

            Member member1 = new Member();
            member1.setUsername("회원1");
            member1.setTeam(teamA);
            em.persist(member1);

            Member member2 = new Member();
            member2.setUsername("회원2");
            member2.setTeam(teamA);
            em.persist(member2);

            Member member3 = new Member();
            member3.setUsername("회원3");
            member3.setTeam(teamB);
            em.persist(member3);

            em.flush();
            em.clear();

//            String query = "select m from Member m";
            //회원1, 팀A(sql)
            //회원2, 팀A(1차캐시)
            //회원3, 팀B(sql)
            //쿼리 3번(select member1~3, select teamA, select teamB)
            //=> N+1문제 : 첫번째 쿼리로 얻은 결과의 수(N)만큼 추가 쿼리 발생

//            String query = "select m from Member m join fetch m.team";
            //inner join으로 쿼리 한번으로 관련된 데이터를 모두 가져옴

            String query = "select t from Team t join fetch t.members";

//            List<Team> result = em.createQuery(query, Team.class)
//                    .getResultList();
//            for (Member member : result) {
//                System.out.println("username = " + member.getUsername()
//                        + " teamName = " + member.getTeam().getName());
//            }

//            List<Member> result = em.createNamedQuery("Member.findByUsername", Member.class)
//                    .setParameter("username", "회원1")
//                    .getResultList();

            int executeUpdate = em.createQuery("update Member m set m.age = 20")
                    .executeUpdate();

//            for (Member member : result) {
//                System.out.println("member = " + member);
//            }
            tx.commit();
        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }

        emf.close();
    }
}
