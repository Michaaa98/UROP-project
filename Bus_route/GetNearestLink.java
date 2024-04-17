package org.example;

import org.matsim.api.core.v01.network.Link;
import org.matsim.api.core.v01.network.Network;
import org.matsim.core.network.NetworkUtils;
import org.matsim.api.core.v01.Coord;
import org.matsim.core.network.io.MatsimNetworkReader;
import org.matsim.core.network.io.NetworkWriter;

import java.util.Collections;


public class GetNearestLink {

    public static void main(String[] args) {

        // read in the MatSim network
        Network network = NetworkUtils.createNetwork();
        new MatsimNetworkReader(network).readFile("C:\\Users\\miche\\IdeaProjects\\test\\bus_network.xml");

        String[] busStops = {
                "1A - Win-Win Boulevard Bus Station",
                "1A - Borey Lamazon Plaza",
                "1A - Kim Li Prek Phnov Over Fly"

        };
        Coord[] stopCoordinates = {
                new Coord(486493.7779925186,1289591.8924035009),
                new Coord(484898.5730670619, 1288248.0304827776),
                new Coord(485503.5373599284,1288320.72083396)

        };

        // Find the nearest link to each coordinate
        for (int i = 0; i < stopCoordinates.length; i++) {
            Coord stopCoordinate = stopCoordinates[i];
            String busStopName = busStops[i];
            Link nearestLink = NetworkUtils.getNearestLink(network, stopCoordinate);
            System.out.println("Bus Stop: " + busStopName);
            System.out.println("Nearest link: " + nearestLink.getId());
        }
    }
}

