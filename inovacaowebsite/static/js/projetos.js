document.addEventListener('DOMContentLoaded', function() {
    // Function to filter projects by status
    function filterStatus(status) {
        const cards = document.querySelectorAll('.card');
        cards.forEach(card => {
            const statusText = card.querySelector('.status-text').textContent;
            if (statusText === status || status === 'All') {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    }

    // Function to search projects
    function searchProject() {
        const searchInput = document.getElementById('search-input').value.toLowerCase();
        const cards = document.querySelectorAll('.card');
        cards.forEach(card => {
            const projectTitle = card.querySelector('h2').textContent.toLowerCase();
            if (projectTitle.includes(searchInput)) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    }

    // Function to load more projects
    function loadMoreProjects() {
        // This is a placeholder. You would typically fetch more projects from the server.
        alert('Load more projects...');
    }

    document.getElementById('filter-status-btn').addEventListener('click', () => {
        document.querySelector('.dropdown-menu').classList.toggle('show');
    });

    document.getElementById('load-more-btn').addEventListener('click', loadMoreProjects);

    window.filterStatus = filterStatus;
    window.searchProject = searchProject;
});