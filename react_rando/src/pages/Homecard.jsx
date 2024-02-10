import React from "react";
import './home.css'
import ReactPlayer from 'react-player'
import { useState,useEffect } from "react";

const Card1 = ({prop}) => {
    const [todos,settodos] = useState([])
    const [renders,setrenders] = useState(0)
    
    useEffect(fetchtodos,[renders])
    useEffect(fetchtodos,[])

    function createTodo(title,duedate) {
        console.log(renders)
        const id = ' ' + new Date().getTime();
        let temp = todos
        setrenders(renders+1)

        todos.push({
            title: title,
            duedate: duedate,
            id: id
        });
        console.log(temp,todos)
        /*settodos(temp)*/

        localStorage.setItem('todos',JSON.stringify(todos));
    }

    function addTodo() {
        console.log('yay')
        const textbox = document.getElementById('todo-title');
        const title = textbox.value;

        const datepicker = document.getElementById('todo-date');
        const duedate = datepicker.value;

        if (todos.length > 7) {
            let temp = todos
            console.log('yipee')
            temp.splice(0,1)
            settodos(temp)
            console.log(todos)
        }

        createTodo(title,duedate);

    }

    function fetchtodos() {
        const savedTodos = JSON.parse(localStorage.getItem('todos'));
        if (Array.isArray(savedTodos)) {
            settodos(savedTodos)
        } else {
                settodos([{
                title: 'Wash up',
                duedate: "2023-13-3",
                        id: 'id1'
            },{
                title: 'Get car',
                duedate: '2020-5-7',
                id: 'id2'
            },{
                title: 'Check dog',
                duedate: '2022-29-10',
                id: 'id3'
            }]);

        }
    }

    return (
        <div className="one-container">
            <div className="one-home">
                <span className="one-toptext">
                    Home
                </span>
                <div className="one-toptitle">
                    Welcome Home
                </div>
                <span style={{fontSize: 14}}>
                    Your hub for whatever this is!
                </span>
            </div>
            <div className="todo-container">
                <div className="todo-add">
                    Got anything Todo?<br />
                    <div className="todo-add-inp">
                        <input id="todo-title" placeholder="Title" /><br />
                        <input id="todo-date" placeholder="Info" />
                    </div>
                    <button onClick={addTodo}>Add Todo</button>
                </div>
                <div className="todos">
                    {todos.map((e)=>(
                        <div>
                            <div className="todo-title">{e.title}</div> 
                            <div className="todo-date">{e.duedate}</div>
                        </div>
                    ))}
                </div>
            </div>
            <div className="nasa-contain" style={{backgroundImage: `url(${prop.url})`,backgroundPosition: '25% 20%', backgroundSize: 'cover'}}>
                <span className="nasatext">
                    <span className="nasatitle">
                        {prop.title}
                    </span><br />
                    {prop.explanation}
                </span><br />
                {prop.media_type === 'video'
                    ? (
                        <div className="video">
                            <ReactPlayer url={prop.url} controls={false} muted={true} playing={true} width={400} height={250} />
                        </div>
                    ) : 
                    console.log()
                }
            </div>
        </div>

    )
}

export default Card1;