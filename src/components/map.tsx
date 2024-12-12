import { useEffect, useState } from 'react';
import { MapContainer, GeoJSON } from 'react-leaflet';


export default function USAMap() {
    
    const [usaLayer, setUsaLayer] = useState(null)
    const [usaComplementLayer, setUsaComplementLayer] = useState(null)

    useEffect(() => {
        async function fetchData() {
            try {
                const response = await fetch('../../geojson/usa.geojson');
                const usa = await response.json();
                setUsaLayer(usa)

                const usaResponse = await fetch('../../geojson/usaComplement.geojson');
                const usaComplement = await usaResponse.json();
                setUsaComplementLayer(usaComplement)
            } catch (error) {
                console.error("Error fetching GeoJSON data:", error);
            }
        }

        fetchData();
    }, []);

    return (
        <MapContainer
            center={[38, -100]}
            zoom={4}
            style={{ height: '100vh', width: '100%' }}
            maxBounds={[
                [-10.499550, -190.276413], // Southwest
                [75.162102, -20.233040]  // Northeast
            ]}
            maxZoom={7}
            minZoom={4}
        >


            {usaLayer && (
                <GeoJSON
                    data={usaLayer}
                    style={{
                        fillColor: '#252527', // Fill color
                        fillOpacity: 0.5,  // Fill transparency
                        color: 'darkgrey',     // Remove outline
                        weight: 1          // Set outline width to 0
                    }}
                />
            )}

            {usaComplementLayer && (
                <GeoJSON
                    data={usaComplementLayer}
                    style={{
                        fillColor: 'black', // Fill color
                        fillOpacity: 1,      // Fill transparency
                        color: 'none',       // Remove outline
                        weight: 0            // Set outline width to 0
                    }}
                />
            )}
        </MapContainer>
    );
}
