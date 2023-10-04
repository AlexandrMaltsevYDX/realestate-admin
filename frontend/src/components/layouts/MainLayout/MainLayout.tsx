import React from "react";
import styles from "./MainLayout.module.scss";
import { Routes, Route, Link } from "react-router-dom";

import Dashbord from "../../../pages/Dashbord/Dashbord";

import RealEstateObjects from "../../../pages/RealEstateObjects/RealEstateObjects";
import RealEstateObjectCreate from "../../../pages/RealEstateObjectCreate/RealEstateObjectCreate";
import RealEstateObjectsAttrs from "../../../pages/RealEstateObjectsAttrs/RealEstateObjectsAttrs";
import RealEstateObjectAttrsDash from "../../../pages/RealEstateObjectAttrsDash/RealEstateObjectAttrsDash";
import RealEstateObjectsCategories from "../../../pages/RealEstateObjectsCategories/RealEstateObjectsCategories";
import RealEstateObjectAddresses from "../../../pages/RealEstateObjectAddresses/RealEstateObjectAddresses";

import Requests from "../../../pages/Requests/Requests";

import Blog from "../../../pages/Blog/Blog";

import Organization from "../../../pages/Organization/Organization";

import Users from "../../../pages/Users/Users";
import Agents from "../../../pages/Agents/Agents";
import Clients from "../../../pages/Clients/Clients";
import UserProfile from "../../../pages/UserProfile/UserProfile";

import SideBar from "../../../ui/SideBar/SideBar";

const MainLayout: React.FC = () => {
    return (
        <div className={styles.MainLayOut}>
            <SideBar layOutStyle={styles.MainLayOut__sidebar} />
            <div className={styles.MainLayOut__content}>
                <Routes>
                    <Route element={<Dashbord></Dashbord>} path="/" />

                    {/* objects */}
                    <Route
                        element={<RealEstateObjects></RealEstateObjects>}
                        path="/objects"
                    />
                    <Route
                        element={
                            <RealEstateObjectCreate></RealEstateObjectCreate>
                        }
                        path="/create_objects"
                    />

                    {/* attr */}
                    <Route
                        element={
                            <RealEstateObjectAttrsDash></RealEstateObjectAttrsDash>
                        }
                        path="/attr-dashbord"
                    />
                    <Route
                        element={
                            <RealEstateObjectsAttrs></RealEstateObjectsAttrs>
                        }
                        path="/attributes"
                    />
                    <Route
                        element={
                            <RealEstateObjectsCategories></RealEstateObjectsCategories>
                        }
                        path="/categories"
                    />
                    <Route
                        element={
                            <RealEstateObjectAddresses></RealEstateObjectAddresses>
                        }
                        path="/addresses"
                    />

                    {/* requests */}
                    <Route element={<Requests></Requests>} path="/request" />

                    {/* blog */}
                    <Route element={<Blog></Blog>} path="/blog" />

                    {/* organiztions */}
                    <Route
                        element={<Organization></Organization>}
                        path="/organiztions"
                    />

                    {/* users */}
                    <Route element={<Users></Users>} path="/users" />
                    <Route element={<Agents></Agents>} path="/agents" />
                    <Route element={<Clients></Clients>} path="/clients" />
                    <Route
                        element={<UserProfile></UserProfile>}
                        path="/my_profile"
                    />
                </Routes>
            </div>
            <div className={styles.MainLayOut__navbar}>Navbar</div>
            <div className={styles.MainLayOut__footer}>Footer</div>
        </div>
    );
};

export default MainLayout;
