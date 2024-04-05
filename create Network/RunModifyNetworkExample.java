/* *********************************************************************** *
 * project: org.matsim.*
 *                                                                         *
 * *********************************************************************** *
 *                                                                         *
 * copyright       : (C) 2017 by the members listed in the COPYING,        *
 *                   LICENSE and WARRANTY file.                            *
 * email           : info at matsim dot org                                *
 *                                                                         *
 * *********************************************************************** *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *   See also COPYING, LICENSE and WARRANTY file                           *
 *                                                                         *
 * *********************************************************************** */

package org.example;

import org.matsim.api.core.v01.network.Link;
import org.matsim.api.core.v01.network.Network;
import org.matsim.core.network.NetworkUtils;
import org.matsim.core.network.io.MatsimNetworkReader;
import org.matsim.core.network.io.NetworkWriter;

import java.util.Collections;


/**
 * @author  jbischoff
 * This provides an example script how to read a MATSim network and modify some values for each link.
 *
 */

public class RunModifyNetworkExample {

    public static void main(String[] args) {

        // read in the network
        Network network = NetworkUtils.createNetwork();
        new MatsimNetworkReader(network).readFile("C:\\Users\\miche\\OneDrive\\Dokument\\urop\\cambodia-latest.osm\\network3.xml.gz");

        // iterate through all links
        for (Link l : network.getLinks().values()){

            l.setAllowedModes(Collections.singleton("car,bus,other,bike"));

        }
        new NetworkWriter(network).write("modified_network.xml");
    }
}