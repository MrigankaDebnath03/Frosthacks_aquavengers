function toggleAnswer(element) {
    const answer = element.nextElementSibling;
    answer.style.display = answer.style.display === 'block' ? 'none' : 'block';
    if (answer.style.display === 'block') {
        // Additional code for solution discussion, e.g., open-ended questions, resources, etc.
        console.log('Let\'s discuss solutions and perspectives for this question. What are your thoughts?');
    }
}
