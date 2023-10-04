import React, { useState } from "react";
import { Link } from "react-router-dom";
import styles from "./SideBarItem.module.scss";

interface SideBarItemProps {
    url?: string;
    name: string;
    subItems?: SideBarItemProps[]; // Nested items
}

const SideBarItem: React.FC<SideBarItemProps> = ({ url, name, subItems }) => {
    const [isExpanded, setIsExpanded] = useState(false);

    const handleToggleExpand = () => {
        setIsExpanded((prevExpanded) => !prevExpanded);
    };

    return (
        <>
            <Link onClick={handleToggleExpand} className={styles.link} to={url}>
                {name}
            </Link>
            <div
                className={
                    isExpanded ? styles.subItemBox_open : styles.subItemBox
                }
            >
                {subItems?.map((subItem, index) => (
                    <SideBarItem
                        key={index}
                        url={subItem.url}
                        name={subItem.name}
                        subItems={subItem.subItems}
                    />
                ))}
            </div>
        </>
    );
};

export default SideBarItem;
