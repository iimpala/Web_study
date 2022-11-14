/* eslint-disable */

import './App.css';
import { useState } from 'react'

function App() {

  let [글제목, 제목변경] = useState(['남자 코트 추천' ,'강남 우동 맛집', '파이썬 독학'])
  let [따봉, 따봉변경] = useState(글제목.map(function(){return 0}))
  let [modal, setModal] = useState(false)
  let [title, setTitle] = useState(0)
  let [input, setInput] = useState('')

  return (
    <div className="App">
      <div className="black-nav">
        <div>React Blog</div>
      </div>
      <div className="list">
        <button onClick={()=>{
          let copy = [...글제목];
          copy[0] = "여자 코트 추천";
          제목변경(copy)
          }}>글 수정</button>

          <button onClick={()=>{
            let copy = [...글제목];
            copy.sort();
            제목변경(copy);
          }}>가나다순 정렬</button>
      </div>
      {
        글제목.map(function(a, i){
          return (
            <div className="list" key={i}>
              <h4 onClick={()=>{
                setModal(!modal)
                setTitle(i)
                }}> { 글제목[i] }

                <span onClick={ (e)=>{
                  e.stopPropagation(); 
                let copy  = [...따봉];
                copy[i] += 1;
                따봉변경(copy)
                }}>👍</span> { 따봉[i] }
              </h4>               
              <p>2월 17일 발행</p>
              <button onClick={(e)=>{
                  e.stopPropagation();
                  let copy = [...글제목]
                  copy.splice(i, 1)
                  제목변경(copy)

                  let copy2 = [...따봉]
                  copy2.splice(i, 1)
                  따봉변경(copy2)
                }}>삭제</button>
            </div>
          )
        })
      }
      
      <input onChange={(e)=>{setInput(e.target.value)}}/>
      <button onClick={()=>{
        let copy = [...글제목]
        copy.unshift(input)
        제목변경(copy)

        let copy2 = [...따봉]
        copy2.unshift(0)
        따봉변경(copy2)
      }}>글 발행</button>
      {
        modal == true ? <Modal title={title} 글제목={글제목} 제목변경={제목변경}/> : null
      }
    
    </div>
  );
}

function Modal(props){
  return (
    <div className='modal' style={{background : props.color}}>
      <h4>{ props.글제목[props.title] }</h4>
      <p>날짜</p>
      <p>상세내용</p>
      <button onClick={()=>{
          let copy = [...props.글제목];
          copy[0] = "여자 코트 추천";
          props.제목변경(copy)
          }}>글 수정</button>

    </div>
  )
}

export default App;
