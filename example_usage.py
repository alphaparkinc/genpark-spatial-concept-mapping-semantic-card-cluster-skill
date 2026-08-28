from client import SpatialConceptMappingSemanticCardClusterClient

def main():
    client = SpatialConceptMappingSemanticCardClusterClient()
    res = client.cluster_knowledge_cards_spatially(36, 'cvs_quantum_cryptography_8812')
    print('Spatial Canvas: ' + res['canvas_session_id'] + ' (' + str(res['cards_clustered_count']) + ' cards)')
    print('Thematic Clusters: ' + ', '.join(res['thematic_sections_identified']))
    print('Semantic Edges: ' + str(res['semantic_edge_links_created']))
    print('Canvas URL: ' + res['whiteboard_export_json_url'])

if __name__ == '__main__':
    main()
