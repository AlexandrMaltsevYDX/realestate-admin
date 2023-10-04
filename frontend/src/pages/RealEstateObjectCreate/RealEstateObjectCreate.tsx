import React from "react";
import styles from "./RealEstateObjectCreate.module.scss";

const RealEstateObjectCreate: React.FC = () => {
    return (
        <div>
            <h1>RealEstateObjectCreate</h1>
            <div id="comertialOrLiving">
                <label htmlFor="comertialOrLiving">Комерческое или Жилое:</label>
                <input
                    type="radio"
                    id="option1"
                    name="comertialOrLiving"
                    value="option1"
                />
                <label htmlFor="option1">Комерческое</label>

                <input
                    type="radio"
                    id="option2"
                    name="comertialOrLiving"
                    value="option2"
                />
                <label htmlFor="option2">Жилое</label>
            </div>
            <div id="newlyOrSecondary">
                <label htmlFor="newlyOrSecondary">Новое или Вторичное:</label>
                <input
                    type="radio"
                    id="option1"
                    name="newlyOrSecondary"
                    value="option1"
                />
                <label htmlFor="option1">Новое</label>
                <input
                    type="radio"
                    id="option2"
                    name="newlyOrSecondary"
                    value="option2"
                />
                <label htmlFor="option2">Вторичное</label>
            </div>
            <div id="typeObject">
                <label htmlFor="typeObject">Тип Объекта: </label>
                <select id="options4" name="options">
                    <option value="option1">Дом</option>
                    <option value="option2">Квартира</option>
                    <option value="option3">Гараж</option>
                </select>
            </div>
            <div id="typeObject">
                <label htmlFor="typeObject">Материал: </label>
                <select id="options4" name="options">
                    <option value="option1">Кирпич</option>
                    <option value="option2">Панелька</option>
                    <option value="option3">Гараж</option>
                </select>
            </div>
            <div id="typeObject">
                <label htmlFor="typeObject">Ландшафт: </label>
                <select id="options4" name="options">
                    <option value="option1">Лесистый</option>
                    <option value="option2">Бугристый</option>
                </select>
            </div>
        </div>
    );
};

export default RealEstateObjectCreate;
