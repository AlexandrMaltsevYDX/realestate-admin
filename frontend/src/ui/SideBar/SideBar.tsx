import React from "react";
import styles from "./SideBar.module.scss";
import SideBarItem from "../SideBarItem/SideBarItem";

interface SidebarProps {
    layOutStyle: string;
}

const SideBar: React.FC<SidebarProps> = ({ layOutStyle }) => {
    const sidebarData = [ // ! add icons to object
        {
            name: "Главная",
            url: "/",
        },
        {
            name: "Управление Объектами",
            url: "/objects",
            subItems: [
                {
                    name: "Объекты",
                    url: "/objects",
                    subItems: [
                        {
                            name: "Редактировать",
                            url: "/objects",
                        },
                        {
                            name: "Создать",
                            url: "/create_objects",
                        },
                    ],
                },
                {
                    name: "Атрибуты",
                    url: "/attr-dashbord",
                    subItems: [
                        {
                            name: "Характеристики",
                            url: "/attributes",
                        },
                        {
                            name: "Категории",
                            url: "/categories",
                        },
                        {
                            name: "Адреса",
                            url: "/addresses",
                        },
                    ],
                },
            ],
        },
        {
            name: "Заявки",
            url: "/request",
        },
        {
            name: "Блог",
            url: "/blog",
        },
        {
            name: "Организация",
            url: "/organiztions",
        },
        {
            name: "Пользователи",
            url: "/users",
            subItems: [
                {
                    name: "Агенты",
                    url: "/agents",
                },
                {
                    name: "Клиенты",
                    url: "/clients",
                },
                {
                    name: "Мой профиль",
                    url: "/my_profile",
                },
            ],
        },
    ];

    return (
        <div className={`${layOutStyle} ${styles.Sidebar}`}>
            {sidebarData.map((item, index) => (
                <SideBarItem
                    key={index}
                    name={item.name}
                    url={item.url}
                    subItems={item.subItems}
                />
            ))}
        </div>
    );
};

export default SideBar;
